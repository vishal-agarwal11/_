import os
import re
import time
import json
import collections
import requests as rq
import logging

# A demo thread program to demonstrate a thread with events.
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)-15s %(message)s')


FireballLocation = collections.namedtuple(
    'FireballLocation', ('date energy impact_e lat lat_dir lon lon_dir alt vel'))


def with_retries(attempts=3, delay=5):
    """
    A decorator will attempt to call a method on which
    this is applied with a given number of times. If the
    values attempts and delay are not provided with call
    of this decor, the default values will be used.
    """
    def decorator(f):
        def inner(*args, **kwargs):
            raise_error = kwargs.pop('raise_error', True)
            logging.info(f"Will attempt {attempts} "
                         f"times to execute {f.__name__}")
            for i in range(attempts):
                logging.info(f"Attempt {i}")
                try:
                    return f(*args, **kwargs)
                except rq.HTTPError as e:
                    logging.error(f"Attempt {i}, Error {e}")
                    time.sleep(delay)
            logging.error(f"Failed to  {f.__name__} in " 
                          f"{attempts} attempts")
            if raise_error:
                raise rq.HTTPError(
                    f"Failed to execute {f.__name__} in {attempts} "
                    f"attempts due to Error")
                
        return inner
    return decorator


class Location:
    """
    This class deals with the input cordinates provided in either
    signed or compass fashion.
    Does return the Location named tuple which is always in 
    compass format
    """            
    def __init__(self):
        self.lat = None
        self.lon = None
        self.lat_dir = None
        self.lon_dir = None

    def __str__(self):
        return (f"latitude: {self.lat}, "
               f"latitude_direction: {self.lat_dir} "
               f"and longitude: {self.lon}, "
               f"longitude_direction: {self.lon_dir}")

    def clean(self, latitude, longitude):
        # Check the latitude and convert into a valid
        # lat and lat dir
        if not (
            isinstance(
                latitude,
                str
                ) and isinstance(
                    longitude,
                    str
                    ) or isinstance(
                        latitude,
                        float
                        ) and isinstance(
                            longitude,
                            float)):
            raise ValueError(
                f"Mixed scheme provided, provide latitude and "
                f"longitude either in sign or compass format.")


        # Compass directions
        if isinstance(
            latitude,
            str) and isinstance(
                longitude,
                str):

            # Check if its a valid compass direction
            lat_ = Location.validate_compass_latitude(latitude)
            lon_ = Location.validate_compass_longitude(longitude)

            # If both latitude and longitude are valid
            if lat_ and lon_:
                self.lat, self.lat_dir = lat_
                self.lon, self.lon_dir = lon_
            else:
                raise ValueError(f"Incompatible latitude or longitude formats")

        ## If the signed directions are given
        ## chaek if its valid or not
        if isinstance(
            latitude,
            float
        ) and isinstance(
            longitude,
            float):

            # check in signed latitude or longitude in range defined
            if not self.validate_signed_latitude(
                latitude
                ) or not self.validate_signed_longitude(
                    longitude
                    ):
                raise ValueError(f"signed latitude should be in "
                                 f" range -90 to 90 "
                                 f"and longitude in -180 to 180")

            self.lat = Location.get_latorlon_value(latitude)
            self.lon = Location.get_latorlon_value(longitude)
            # Convert the singed longidude and longitude to
            # compass latitude and longitude
            self.lat_dir, self.lon_dir = Location.signed_to_compass_direction(
                latitude,
                longitude)

    @staticmethod
    def signed_to_compass_direction(latitude, longitude):
        if latitude > 0 and longitude < 0:
            return "N", "W"
        elif latitude < 0 and longitude < 0:
            return "S", "W"
        elif latitude < 0 and longitude > 0:
            return "S", "E"
        elif latitude > 0 and longitude > 0:
            return "N", "E"
        else:
            return None


    @staticmethod
    def validate_signed_latitude(value):
        return -90 <= value <= 90

    @staticmethod
    def validate_signed_longitude(value):
        return -180 <= value <= 180

    @staticmethod
    def validate_compass_latitude(value):
        lat = Location.get_latorlon_value(value)
        lat_dir = Location.get_compass_dir(value)
        if 0 <= lat <= 90 and\
            lat_dir in ["N", "S"]:
            return lat, lat_dir
        return None

    @staticmethod
    def validate_compass_longitude(value):
        lon = Location.get_latorlon_value(value)
        lon_dir = Location.get_compass_dir(value)
        if 0 <= lon <= 180 and\
            lon_dir in ["W", "E"]:
            return lon, lon_dir
        return None

    @staticmethod
    def get_compass_dir(lat_lon_dir):
        """
        Return the compass direction if given
        """
        compass_dir_regex = re.compile(
            r"(?P<compass_direction>[a-zA-Z]+)")

        try:
            resp = compass_dir_regex.search(lat_lon_dir)
            if resp:
                return resp.group("compass_direction")
        except ValueError as e:
            logging.error(f"An error occured while getting the compass "
                          f"direction, {e}")
        return None


    @staticmethod
    def get_latorlon_value(lat_lon_value):
        """
        This method get the actual direction values
        """
        if not isinstance(lat_lon_value, str):
            lat_lon_value = str(lat_lon_value)
    
        val_dir_regex = re.compile(
            r"(?P<direction>[0-9.]+)")

        try:
            resp = val_dir_regex.search(lat_lon_value)
            if resp:
                return float(resp.group("direction"))
        except ValueError as e:
            logging.error(f"An error occured while getting direction, {e}")
        return None


class Fireball:
    # API_URL - keeping it class varible so that in case of API_URL change
    # a class method changes the url for all the objects getting instantiated.
    API_URL = "https://ssd-api.jpl.nasa.gov/fireball.api"

    @classmethod
    def set_api_url(cls, new_api_url):
        """
        In case of API Change, will use this method to make the
        changes affected to every object being instantiated.
        """
        cls.API_URL = new_api_url
    
    def __init__(self, *args, **kwargs):
        self.date_min = kwargs.get("date_min", None)
        self.date_max = kwargs.get("date_max", None)
        self.buffer = kwargs.get("buffer", 15)
        self.req_alt = kwargs.get("req_alt", False)

    @property
    def coordinate_buffer(self):
        return self.buffer

    @coordinate_buffer.setter
    def coordinate_buffer(self, val):
        self.buffer = val

    @property
    def mindate(self):
        return self.date_min

    @property
    def maxdate(self):
        return self.date_max

    @mindate.setter
    def mindate(self, val):
        self.date_min = val

    @maxdate.setter
    def maxdate(self, val):
        self.date_max = val

    def url_seperator(self, url):
        return "&" if "?" in url else "?"

    @with_retries()
    def get_shine_date(self, location, *args, **kwargs):

        if not isinstance(location, Location):
            raise TypeError("{location} is not an object of Location")

        self.date_min = kwargs.get("date_min", self.date_min) 
        self.date_max = kwargs.get("date_max", self.date_max)
        self.req_alt = kwargs.get("req_alt", self.req_alt)

        api = f"{self.API_URL}"
        if self.date_min:
            api += f"{self.url_seperator(api)}date-min={self.date_min}"

        if self.date_max:
            api += f"{self.url_seperator(api)}date-max={self.date_max}"

        if self.req_alt:
            api += f"{self.url_seperator(api)}req-alt={self.req_alt}"

        print(f"Getting data from {api}")
        rs = rq.get(api)
        res_data = json.loads(rs.text)
        logging.info(f"Finding the brightest fireball at location "
                     f"with latitude: {location.lat}, "
                     f"latitude direction: \"{location.lat_dir}\" "
                     f"longitude: {location.lon}, "
                     f"longitude direction: \"{location.lon_dir}\"")

        max_bright_energy = 0
        bright_fireball = None

        lower_lat = 0 if location.lat - self.buffer < 0 else location.lat - self.buffer
        upper_lat = 90 if location.lat + self.buffer > 90 else location.lat + self.buffer
        lower_lon = 0 if location.lon - self.buffer < 0 else location.lon - self.buffer
        upper_lon = 180 if location.lon + self.buffer > 180 else location.lon + self.buffer

        for data in res_data["data"]:
            try:
                if (
                    location.lat_dir == data[4] and location.lon_dir == data[6]
                    ) and (
                        float(data[1]) > max_bright_energy
                        ) and (
                            lower_lat <= float(data[3]) <= upper_lat
                            ) and (
                                lower_lon <= float(data[5]) <= upper_lon):
                    bright_fireball = FireballLocation(*data)
            except KeyError as key_error:
                logging.error(key_error)
        return bright_fireball


def units():
    """
    Unit Tests
    """
    compass_locations = [
        "42.354558N",
        "45.354558S",
        "42.354558Z",
        "122.4039064 W",
        "122.4039064 E",
        "122.4039064E",
        "270.4039064N"]
    
    signed_locations = [
        -85.73647483,
        -105.7365437,
        88.83475846,
        99.47584582,
        270.7267832,
        -350.7634743]

    ## Unit Tests
    def test_compass_latitudes():
        logging.info(f"Testing valid compass latitudes in {compass_locations}")
        for latitude in compass_locations:
            if Location.validate_compass_latitude(latitude) != None:
                logging.info(f"Valid latitude- {latitude}")
            else:
                logging.error(f"Invalid latitude- {latitude}")
            
    def test_compass_longitudes():
        logging.info("\n\n")
        logging.info(f"Testing valid compass longitudes in {compass_locations}")
        for longitude in compass_locations:
            if Location.validate_compass_longitude(longitude):
                logging.info(f"Valid longitude: {longitude}")
            else:
                logging.error(f"Invalid longitude: {longitude}")

    def test_signed_latitudes():
        logging.info("\n\n")
        logging.info(f"Testing valid signed latitudes in {signed_locations}")
        for latitude in signed_locations:
            if Location.validate_signed_latitude(latitude):
                logging.info(f"Valid latitude: {latitude}")
            else:
                logging.error(f"Invalid latitude: {latitude}")

    def test_signed_longitudes():
        logging.info("\n\n")
        logging.info(f"Testing valid signed longitudes in {signed_locations}")
        for longitude in signed_locations:
            if Location.validate_signed_longitude(longitude):
                logging.info(f"Valid longitude: {longitude}")
            else:
                logging.error(f"Invalid longitude: {longitude}")

    test_compass_latitudes()
    test_compass_longitudes()
    test_signed_latitudes()
    test_signed_longitudes()



if __name__ == "__main__":
    os.system("clear")
    units()
    
    ## Inputs Start
    start_date = "2019-01-01"
    end_date = "2020-06-30"
    
    location_data =  """
    Boston -        latitude: 42.354558N, longitude:  71.054254W
    NCR -           latitude: 28.574389N, longitude:  77.312638E
    San Francisco - latitude: 37.793700N, longitude: 122.403906W"""
    ## Inputs End

    logging.info(f"Lets figure out the brightest star among {location_data}")

    loc_data_regex = re.compile(
        r"\n*\s*(?P<location>[a-zA-Z\s+]*)\s+-"
        r"\s+latitude:\s+(?P<latitude>[A-Z0-9.]+)"
        r",\s+longitude:\s+(?P<longitude>[A-Z0-9.]+)")

    locations = loc_data_regex.findall(location_data)

    brightest_fireball_energy = 0
    brightest_fireball = None
    brightest_fireball_city = None
    
    for location in locations:
        loc = Location()
        loc.clean(*location[1:])
        
        logging.info(f"\n\nFinding fireball brightness at {location[0]}")
        bright_fireball = Fireball().get_shine_date(
            loc,
            date_min=start_date,
            date_max=end_date,
            req_alt=True)
        
        if bright_fireball:
            logging.info(f"The brightest fireball energy at "
                         f"{location[0]} was {bright_fireball.energy} "
                         f"on {bright_fireball.date}.")
            if float(bright_fireball.energy) > brightest_fireball_energy:
                brightest_fireball = bright_fireball
                brightest_fireball_city = location[0]
        else:
            logging.error(f"There was no fireball at {location[0]}")

    if brightest_fireball:
        logging.info(f"\n\nThe brightest fireball was at "
                     f"{brightest_fireball_city} on "
                     f"{brightest_fireball.date} with "
                     f"energy {brightest_fireball.energy}")
    
    signed_loc = Location()
    signed_loc.clean(-88.73647483, 75.73647483)
    print(signed_loc)

# 
# Your previous Python 2 content is preserved below:
# 
# def say_hello():
#     print 'Hello, World'
# 
# for i in xrange(5):
#     say_hello()
# 
# 
# # 
# # Your previous Plain Text content is preserved below:
# # 
# # ===== Preface =====
# # 
# # This question is very difficult in C and C++, where there is
# # insufficient library support to answer it in an hour. If you
# # prefer to program in one of those languages, please ask us to
# # provide you with a question designed for those languages instead!
# # 
# # 
# # ===== Intro =====
# # 
# # Here at Delphix, we admire NASA’s engineering mission. But beyond
# # that, we can use data from NASA to learn about how space interacts
# # with Earth. Solving global warming is unfortunately outside the scope
# # of an interview question, so your goal is somewhat simpler: use
# # NASA’s public HTTP APIs to create a function which determines which
# # of three locations has seen the brightest shooting stars in 2019.
# # This can be handy if you're trying to find a good spot to do some night sky
# # watching. :-)
# # 
# # You should implement this in whatever language you're most
# # comfortable with -- just make sure your code is commented,
# # has error handling, and is modularized if possible.
# # 
# # Finally, please help us by keeping this question and your
# # answer secret so that every candidate has a fair chance in
# # future Delphix interviews. Thank you!
# # 
# # 
# # ===== Steps =====
# # 
# # 1.  Choose the language you want to code in from the menu
# #     labeled "Plain Text" in the top right corner of the
# #     screen. You will see a "Run" button appear on the top
# #     left -- clicking this will send your code to a Linux
# #     server and compile / run it. Output will appear on the
# #     right side of the screen.
# #     
# #     For information about what libraries are available for
# #     your chosen language, see:
# # 
# #       https://coderpad.io/languages
# # 
# # 2.  Pull up the documentation for the API you'll be using:
# # 
# #       https://ssd-api.jpl.nasa.gov/doc/fireball.html
# # 
# # 3.  Implement a function fireball() whose function signature
# #     looks like this (can differ slightly depending on the
# #     language you chose):
# # 
# #       float fireball(double latitude, double longitude)
# # 
# #     When there is enough data to do so, the function should
# #     return the brightness and location for the brightest shooting 
# #     star seen in 2019 at the given location.
# # 
# #     The human eye can see a lot of the night sky, so give your latitude
# #     and longitude a buffer of +/- 15. For example, if you are looking
# #     for shooting stars at the Delphix SF Office 
# #          37.7937007 N,  122.4039064 W
# #     You would look for shooting stars within these coordinates: 
# #          (22.7937007   <--> 52.7937007 N,
# #          107.4039064 <--> 137.4039064 W)
# # 
# #     *Note* that Latitude and Longitude can be written in a few different
# #     formats. We suggest either using Signed Degrees, or Degrees plus
# #     Compass Direction:
# # 
# #     Signed Degrees:
# #      - Latitudes range from -90 to 90.
# #      - Longitudes range from -180 to 180.
# #      
# #     Degrees plus Compass Direction:
# #     Latitudes range from 0 to 90.
# #     Longitudes range from 0 to 180.
# #     Use N, S, E or W as either the first or last character, which
# #     represents a compass direction North, South, East or West.
# # 
# #     The brightness should be determined using the energy from each
# #     shooting star (a higher ‘energy’ meaning a brighter star).
# #     
# #     You can use the https://ssd-api.jpl.nasa.gov/doc/fireball.html API
# #     to get the information you will need to compute this.
# # 
# # 4.  With your fireball() function, determine which of three
# #     locations had the brightest shooting star in
# #     2019. Print out the location and brightness for that star.
# # 
# #     Use these Delphix Office Locations to figure out which Office
# #     saw the brightest star in 2019 (2019-01-01 -> 2020-01-01)
# # 
# # 
# #     Boston -        latitude: 42.354558N, longitude:  71.054254W
# #     NCR -           latitude: 28.574389N, longitude:  77.312638E
# #     San Francisco - latitude: 37.793700N, longitude: 122.403906W
# # 
# # 
# # 5.  Add any tests for your code to the main() method of
# #     your program so that we can easily run them.
# # 
# # 6.  Don’t forget to implement error handling. Depending on the language
# #     you are using, feel free to adjust the function signature to do it in an
# #     idiomatic way (e.g Exceptions in Java)
# # 
# # 
# # 
# # ====== FAQs =====
# # 
# # Q:  Won't we be able to see a wider longitude range the higher our latitude
# #     (with an extreme of either the North or South Pole)?
# # A:  That is correct. But to help simplify this problem you can just assume
# #     that we can only see the +/- 15 degrees regardless of your location.
# # 
# # Q:  How do I know if my solution is correct?
# # A:  Make sure you've read the prompt carefully and you're
# #     convinced your program does what you think it should
# #     in the common case. If your program does what the prompt 
# #     dictates, you will get full credit. We do not use an
# #     auto-grader, so we do not have any values for you to
# #     check correctness against.
# # 
# # Q:  What is Delphix looking for in a solution?
# # A:  After submitting your code, we'll have a pair of engineers
# #     evaluate it and determine next steps in the interview process.
# #     We are looking for correct, easy-to-read, robust code.
# #     Specifically, ensure your code is idiomatic and laid out
# #     logically. Ensure it is correct. Ensure it handles all edge
# #     cases and error cases elegantly.
# #     
# # Q:  How should my output be formatted?
# # A:  Your output should include a location and the energy of the
# #     star in whatever format you find easiest. There are no other
# #     strict formatting constraints (we just inspect the output for
# #     correctness).
# # 
# # Q:  Any suggestions of fun locations I can test with?
# # A:  Sure! Here are a few:
# # 
# #     Fun location           Latitude    Longitude
# #     ---------------------  ----------  ------------
# #     Grand Canyon           36.098592N   112.097796W
# #     Niagara Falls          43.078154N   79.075891W
# #     Four Corners Monument  36.998979N   109.045183W
# #     Delphix San Francisco  37.7937007N  122.4039064W
# # 
# # Q:  If I need a clarification, who should I ask?
# # A:  Send all questions to the email address that sent you
# #     this document, and an engineer at Delphix will get
# #     back to you ASAP (we're pretty quick during normal
# #     business hours).
# # 
# # Q:  How long should this question take me?
# # A:  Approximately 1 hour, but it could take more or less
# #     depending on your experience with web APIs and the
# #     language you choose.
# # 
# # Q:  When is this due?
# # A:  We will begin grading your answer 24 hours after it is
# #     sent to you, so that is the deadline.
# # 
# # Q:  How do I turn in my solution?
# # A:  Anything you've typed into this document will be saved.
# #     Email us when you are done with your solution. We will
# #     respond confirming we've received the solution within
# #     24 hours.
# # 
# # Q:  Can I use any external resources to help me?
# # A:  Absolutely! Feel free to use any online resources you
# #     like, but please don't collaborate with anyone else.
# # 
# # Q:  Can I use my favorite library in my program?
# # A:  Unfortunately, there is no way to load external
# #     libraries into CoderPad, so you must stick to what
# #     they provide out of the box for your language (although
# #     they do support for many popular general-use libraries):
# # 
# #       https://coderpad.io/languages
# # 
# #     If you really want to use something that's not
# #     available, email the person who sent you this link
# #     and we will work with you to find a solution.
# # 
# # Q: Can I code this up in a different IDE?
# # A: Of course! However, we do not have your environment
# #     to run your code in. We ask that you submit your final
# #     code via CoderPad (and make sure it can run). This gives
# #     our graders the ability to run your code rather than guessing.
# # 
# # Q:  Why does my program terminate unexpectedly in
# #     CoderPad, and why can't I read from stdin or pass
# #     arguments on the command line?
# # A:  CoderPad places a limit on the runtime and amount of
# #     output your code can use, but you should be able to
# #     make your code fit within those limits. You can hard
# #     code any arguments or inputs to the program in your
# #     main() method or in your tests.
# # 
# # Q:  I'm a Vim/Emacs fan -- is there any way to use those
# #     keybindings? What about changing the tab width? Font
# #     size?
# # A:  Yes! Hit the button at the bottom of the screen that
# #     looks like a keyboard.
# # 
# # 
# # 
# 

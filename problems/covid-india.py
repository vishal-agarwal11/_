import json
import requests
from datetime import datetime


class Covid:
    def __init__(self):
        self.api_url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india_timeline"
        self.es_url = "http://10.145.68.212:9200/covid19/India"
        self.headers = {
            'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
            'x-rapidapi-key': "70ea83bd4bmsh68c7b5c1ac58be1p12899djsnf077076a9195"
            }


    def get_datetime(self, inp_date):
        map_ = {
            "January":"01",
            "February":"02",
            "March":"03",
            "April":"04",
            "May":"05",
            "June":"06",
            "July":"07"
            }
        inp_date = inp_date.split(" ")
        if len(inp_date) == 3:
            inp_date.pop(-1)

        op_date = datetime.strptime(
            f"2020-{map_[inp_date[-1]]}-{inp_date[0]} 23:00:00",
            "%Y-%m-%d %H:%M:%S").isoformat()
        return op_date

    def getdata(self):
        self.response = requests.request(
            "GET",
            self.api_url,
            headers=self.headers)

    def espush(self, index=-1):
        headers = {"Content-Type": "application/json"}
        self.getdata()
        if not index:
            for ele in json.loads(self.response.text):
                ele["@timestamp"] = self.get_datetime(ele["date"])
                ele["dailyconfirmed"] = int(ele["dailyconfirmed"])
                ele["dailydeceased"] = int(ele["dailydeceased"])
                ele["dailyrecovered"] = int(ele["dailyrecovered"])
                ele["totalconfirmed"] = int(ele["totalconfirmed"])
                ele["totaldeceased"] = int(ele["totaldeceased"])
                ele["totalrecovered"] = int(ele["totalrecovered"])
                del(ele["date"])
                res = requests.post(
                    self.es_url,
                    data=json.dumps(ele),
                    headers=headers)
                print(f"Document insert response code {res.status_code}, text {res.text}")
        else:
            res = requests.post(
                self.es_url,
                data=json.dumps(ele[index]),
                headers=headers)
            print(f"Document insert response code {res.status_code}, text {res.text}")


if __name__ == "__main__":
    covid = Covid()
    covid.espush(index=None)

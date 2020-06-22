class Device(object):
    @classmethod
    def determine_type(cls, type_, *args, **kwargs):
        return eval(type_)(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        self.hostname = kwargs.get("hostname", "localhost")
        self.username = kwargs.get("username", "admin")

    def __str__(self):
        return f"{self.__class__.__name__}:{self.username}@{self.hostname}"


class Cisco(Device):
    def __init__(self, *args, **kwargs):
        self.vendor = "Cisco"
        super().__init__(*args, **kwargs)


class Brocade(Device):
    def __init__(self, *args, **kwargs):
        self.vendor = "Brocade"
        super().__init__(*args, **kwargs)


if __name__ == "__main__":
    obj = Device.determine_type(
        "Cisco",
        hostname="org.cisco.rnd.com",
        username="superadmin")

    obj1 = Device.determine_type("Brocade")
    print(f"Device_1 = {obj}\nDevice_2 = {obj1}")
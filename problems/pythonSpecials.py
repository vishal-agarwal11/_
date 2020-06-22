class Device:
    def __init__(self):
        self.username = "root"
        self.ip = "192.168.120.10"
        self.device = "Linux"

    def __repr__(self):
        """
        called upon inspect
        """
        return f"Test"

    def __str__(self):
        """Called upon calling a print upon the object"""
        return f"{self.device}/{self.username}@{self.ip}"


class RawDevice:
    def __init__(self):
        pass


if __name__ == "__main__":
    print(RawDevice())
    print(Device())
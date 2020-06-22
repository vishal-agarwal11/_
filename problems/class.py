class Device:
    def __init__(self):
        self.ip = None
        pass

    @property
    def deviceip(self):
        return self.ip

    @deviceip.setter
    def deviceip(self, value):
        self.ip = value 
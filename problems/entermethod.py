from pprint import pprint
class Device(object):
    def __init__(self, ip, username= "root"):
        print("__init__")
        self.ip = ip
        self.username = username

    def __enter__(self): 
        print("__enter__")
        return self

    def connect(self):
        print(f"connecting to {self.username}@{self.ip}")

    def __exit__(self, type, value, traceback):
        print("__exit__")

    def __del__(self):
        print("__del__")

#with Device("192.168.120.10") as device:
#    device.connect()


import contextlib

@contextlib.contextmanager
def writefile(filename, mode):
    fd = open(filename, mode)
    yield fd
    fd.close


with writefile("hello.txt", "w") as fd:
    fd.write("kdnswncckdnwlkcn")







class Device:
    def __init__(self, ipaddress):
        print(f"__init__ with {ipaddress}")
        self.ipaddress = ipaddress

    def __call__(self, ipaddress):
        print(f"__call__ with {ipaddress}")
        self.ipaddress = ipaddress

    @property
    def getname(self):
        return self.ipaddress


if __name__ == "__main__":
    x = Device("192.168.120.10")
    print(x.getname)
    x("192.168.120.20")
    print(x.getname)
    x("192.168.120.30")
    print(x.getname)



class Example(object):
    def __init__(self):
        self.factorial = {}
        
    def __call__(self, value):
        if value not in self.factorial.keys():
            print "calling factorial method"            
            self.factorial[value] =  self.fact(value)
        return self.factorial[value]


    def fact(self, number):
        if number == 1:
            return 1        
        else:
            return number * self.fact(number-1)


if __name__ == "__main__":
    e = Example()

    print e(3)
    print e(4)
    print e(5)
    print e(3)
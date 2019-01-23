# this is test comment
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

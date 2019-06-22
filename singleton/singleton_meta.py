"""
    This is singleton class example using metaclass.
"""

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BaseClass:
    def __init__(self):
        """Base class Init"""


class MyClass(BaseClass, metaclass=Singleton):
    def __init__(self, *args, **kwargs):
        super(MyClass, self).__init__(*args, **kwargs)


class MyClass1(metaclass=Singleton):
    """Another class"""


if __name__ == "__main__":
    m = MyClass()
    n = MyClass()
    o = type(m)()

    print(m,'\n',n,'\n',o)
    print(list(map(lambda x: id(x), [m, n, o])))
    print(m==n==o)


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
    def __init__(self):
        super(MyClass, self).__init__()


class MyClass1(metaclass=Singleton):
    """Another class"""


if __name__ == "__main__":
    print(MyClass())
    print(MyClass())


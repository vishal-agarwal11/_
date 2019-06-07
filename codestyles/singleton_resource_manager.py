
__author__ = "Sanjeev Rohila"
__license__ = ""
__maintainer__ = "Sanjeev Rohila"
__email__ = "justsanjeev@gmail.com"

class Cluster(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Cluster, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class BlueCluster(metaclass=Cluster):
    def __init__(self):
        """
        How we can leverage a singleton class to leverage
        a container or collection of multiple objects
        creating a resource
        """
        self.container = []

    def __str__(self):
        return f"{__class__}{__class__.__module__}"
    def get(self, b, **kwargs):
        self.container.append(resource(b).get())
        return self.container
    def __del__(self):
        print(f"{self} {__class__.__module__}")
        
class resource:
    def __init__(self, b):
        self.b = b
        print(f"{self} --INIT--")
    def __str__(self):
        return f"{__class__}{__class__.__module__}"
    def get(self):
        obj = iter(range(self.b))
        print(type(obj))
        return obj
    def __del__(self):
        print(f"{self} --DELETE--")


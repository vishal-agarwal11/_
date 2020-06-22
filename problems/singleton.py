class Cluster(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Cluster, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ICluster(metaclass=Cluster):
    def __init__(self):
        pass





ic = ICluster()
ic1 = ICluster()

assert ic == ic1
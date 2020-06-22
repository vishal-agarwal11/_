from pprint import pprint


class Host:
    def __init__(self):
        print(f"__init__ {self.__class__.__name__}")

    def client(self):
        """
        """


class Master(Host):
    def __init__(self, *args, **kwargs):
        print(f"__init__ {self.__class__.__name__}")
        super().__init__(*args, **kwargs)


if __name__ == "__main__":
    master = Master()
    pprint(dir(Master.mro))
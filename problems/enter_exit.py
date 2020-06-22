class Host:
    def __init__(self, ipaddress, username, password):
        print(f"IN __init__")
        self.ipaddress = ipaddress
        self.username = username
        self.password = password

    def __str__(self):
        return f"Host-{self.ipaddress}/{self.username}:{self.password}"

    def method_x(self):
        """
        some class operation
        """
        print(f"###IN method_x####")

    def __del__(self):
        """
        close the connections
        dereference the object etc.
        """
        print(f"IN __del__")

    def __enter__(self):
        print("IN __enter__")
        return self

    def __exit__(self, type, value, traceback):
        print(f"IN __exit__")     


if __name__ == "__main__":
    with Host("10.10.10.10", "root", "pass") as ob:
        print(ob)
        ob.method_x()
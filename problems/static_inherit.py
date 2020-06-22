class StaticBase:
    @staticmethod
    def interest(money, rate, time):
        return money*(1 + rate*time)

    def __init__(self, money, rate, time):
        """"""


class StaticChild(StaticBase):
    """"""


if __name__ == "__main__":
    print(StaticChild.interest(1000, 5, 5))
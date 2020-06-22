class Player:
    membership = True

    def __init__(self, name):
        if Player.membership:
            self.name = name
        else:
            raise RuntimeError("No membership is Open, Try again later!!")



    @classmethod
    def sum(cls, a, b):
        print(cls.__name__)
        return a + b


    @staticmethod
    def sub(a,b):
        print("Player")
        return a - b


p = Player("Akshay")

print(p.sum(1,2))  
print(Player.sum(1,2))


print(Player.sub(5 , 4))
print(p.sub(5 , 4))


class HockeyPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def sub(x,y):
        print("HockeyPlayer")
        return x -y

    @classmethod
    def sum(cls, a, b):
        print(cls.__name__)
        return a + b

hp = HockeyPlayer("Sara")

print(hp)


print(HockeyPlayer.sub(10,2))
print(HockeyPlayer.sum(3,10))
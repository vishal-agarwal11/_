def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class MyClass:
    pass


m = MyClass()
n = MyClass()
o = type(n)()

print(list(map(lambda x: id(x), [m,n,o])))
print(m,'\n',n,'\n',o)
print(m==n==o)
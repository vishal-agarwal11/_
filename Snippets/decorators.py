import time

def decorator(func):
    def inner(a,b):
        for i in range(3):
            func(a,b)
    return inner


@decorator
def test(a,b):
    print(a,b)



def with_retries(retries=3, interval=1):
    def param_decor(func):
        def inner(a, b):
            for i in range(retries):
                func(a, b)
                time.sleep(interval)
        return inner
    return param_decor


@with_retries(5,2)
def test(a,b):
    print(a,b)


test(10,20)
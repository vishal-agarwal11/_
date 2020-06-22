def kangaroo(x1, v1, x2, v2):
    print(x1, v1, x2, v2)
    while True:
        if x1 == x2:
            return "YES"
        if x2 >= 10000 or x1 >= 10000:
            return "NO"
        x1+=v1
        x2+=v2


print(kangaroo(4523, 8092, 9419, 8076))



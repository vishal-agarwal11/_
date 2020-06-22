def sg(number):
    if number <= 9:
        return number
    else:
        return sg(number % 10 + sg(int(number/10)))


print(sg(6789))
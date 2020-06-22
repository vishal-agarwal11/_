def fib_series(n):
    series = []
    i = 0
    while len(series) < 5:
        if i <= 1:
            series.append(i)
        else:
            series.append(series[i-1] + series[i-2])
        i+=1
    return series


#print(fib_series(5))


def fibnocci(n):
    if n in [0, 1]:
        return n
    else:
        return fibnocci(n-1) + fibnocci(n-2)


#res = fibnocci(5)
#print(res)


def fs(n, list()):
    series = []
    if n in [0, 1]:
        series.append(n)
    else:
        series.append(fs(n-1, series)+fs(n-2, series))
    return series

res = fs(5)
print(res)
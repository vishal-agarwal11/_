def permutationEquation(p):
    l = list()
    for x in range(1,len(p)+1):
        for i in range(1,len(p)+1):
            t = p[i-1]
            if p[t-1]==x:
                l.append(i)
    return l



print(permutationEquation([5,2,1,3,4]))
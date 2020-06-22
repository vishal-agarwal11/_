
def FO(s):
    for i in range(len(s)):
        substr = s[i+1:]
        fi = -1
        try:
            f_i = substr.index(s[i])
            return f_i + 1
        except:pass

    return -1


print(FO("abcdeffia"))
def anagram_check(a,b):
    l_a = len(a)
    l_b = len(b)


    d_a, d_b = {}, {}

    for i in range(l_a if l_a >= l_b else l_b):
        try:
            d_a[a[i]]+=1
        except KeyError:
            d_a[a[i]] = 1
        except IndexError:
            pass

        try:
            d_b[b[i]]+=1
        except KeyError:
            d_b[b[i]] = 1
        except IndexError:
            pass

    for key in d_a:
        try:
            if d_a[key] == d_b[key]:
                pass
        except KeyError:
            print(f"{a}, {b} are not Anagrams!")
            return       
    print(f"{a}, {b} are Anagrams!")


anagram_check("army", "ary")

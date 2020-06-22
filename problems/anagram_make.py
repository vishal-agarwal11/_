
a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"

def makeAnagram(a, b):
    a_l = len(a)
    b_l = len(b)
    a_s = {}
    b_s = {}
    
    for i in range(a_l if a_l >= b_l else b_l):
        try:
            a_s[a[i]]+=1
        except KeyError:
            a_s[a[i]] = 1
        except IndexError:
            pass
            
        try:
            b_s[b[i]]+=1
        except KeyError:
            b_s[b[i]] = 1
        except IndexError:
            pass
    

    common = 0
    for key in a_s:
        try:
            common+=min(a_s[key], b_s[key])
        except:pass

    return a_l + b_l - 2 * common


print(makeAnagram(a,b))




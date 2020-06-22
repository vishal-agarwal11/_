


def encodeStr(string):
    encodedStr = ""
    previous = ""
    count  = 0
    for ele in string:
        if ele == previous:
            count+=1
        elif ele != previous and len(previous) != 0:
            if count == 1:
                encodedStr+=previous
            else:
                encodedStr+=previous+str(count)
            previous = ele
            count = 1
        else:    
            previous = ele
            count+=1

    if count > 1:
        encodedStr+=ele+str(count)
    else:
        encodedStr+=previous
    return encodedStr

print(encodeStr("ABABABA"))


from pprint import pprint
def recordWeight(weights, ele, count):
    wt = ord(ele)%96
    key = ele*count
    weights[key] = wt * count

def encodeStr1(string):
    weights = {}
    previous = ""
    count = 0
    for ele in string:
        if ele == previous:
            count+=1
            recordWeight(weights, ele, count)
        elif ele != previous and len(previous) != 0:
            recordWeight(weights, previous, count)

            previous = ele
            count = 1
            recordWeight(weights, previous, count)
        else: 
            previous = ele
            count+=1
            recordWeight(weights, ele, count)
    
    recordWeight(weights, ele, count)

    pprint(weights)


#encodeStr1("aaabbbb")




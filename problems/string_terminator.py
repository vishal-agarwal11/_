def stripper(string, point):
    pre, post = "", ""
    try:
        pre = string[0:point]
    except IndexError:
        pass

    try:
        post = string[point+2:]
    except IndexError:
        pass
    return pre + post


def terminator(string):

    i = 0
    while i < len(string):
        if "#" not in string:
            return string
        elif len(string) >= 2 and "#" not in string[1:]:
            return string.replace("#", "")
        elif len(string) == 1 and string[0] == "#":
            return ""
        elif len(string) == 1:
            return string
        elif len(string) == 2 and string[0] == "#":
            string = string.replace("#", "")
        elif string[i] != "#" and string[i+1] == "#":
            string = stripper(string, i)
            continue
        i+=1
    print(f"Self terminating string is \"{string}\"")
    return string


print(terminator("#ab#c"))
        
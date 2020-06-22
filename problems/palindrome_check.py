

def palindrome(string):
    j = len(string) - 1
    for i in range(int(len(string)/2)):
        if string[i] == string[j]:
            j-=1
        else:
            print(f"{string} is not palindrome")
            return
    print(f"{string} is palindrome")


palindrome("abcdeedcbaz")
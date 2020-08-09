"""
This finction finds out the string on non repeatative letters
and return the length of longest  non repeatative letter string
"""
def longest_substr_no_repeat(string):
    seen = []
    substrings = []
    longest_len = 0

    for i in range(len(string)):
        this_str = ""
        for j in range(i, len(string)):
            if string[j] not in seen:
                this_str += string[j]
                seen.append(string[j])
                if j == len(string) -1:
                    substrings.append(this_str)
                    seen = []
                    if len(this_str) > longest_len:
                        longest_len = len(this_str)
                    break
            else:
                substrings.append(this_str)
                seen = []
                if len(this_str) > longest_len:
                    longest_len = len(this_str)
                break
    
    print(substrings)
    return longest_len

print(longest_substr_no_repeat("abcdabeudgeui"))

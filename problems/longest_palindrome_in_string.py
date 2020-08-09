"""
This program find the length of longest palindrome
in a string, also prints all the palindrome in string
"""


def is_palindrome(string):
    return string == string[::-1]


def longest_palindrome(string):
    palindromes = []
    longest_palindrome = 0
    for i in range(1, len(string)-1):
        r = i - 1
        f = i + 2
        l_s = None
        while r >= 0 or f <= len(string):
            if is_palindrome(string[r:f]):
                l_s = string[r:f]
                len_l_s = len(l_s)
                if r == 0:
                    if len_l_s > longest_palindrome:
                        longest_palindrome = len_l_s
                    palindromes.append(l_s)
                    l_s = None
                    break
                r -= 1
                f += 1
                continue
            elif l_s:
                if len_l_s > longest_palindrome:
                    longest_palindrome = len_l_s
                palindromes.append(l_s)
                l_s = None
                break
            else:
                break
        if l_s:
            palindromes.append(l_s)
            l_s = None

    print(palindromes)
    return longest_palindrome


if __name__ == '__main__':
    sample = "zppnppfehvdfihoidxyzyxituriutiogabattunznutt"
    print(longest_palindrome(sample))

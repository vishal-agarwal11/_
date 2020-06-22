class Solution:
    # The code determines after how many characters
    # are rqquired to be added in the start to make
    # it a palindrome
    
    # @param A : string
    # @return an integer
    def is_palindrome(self, string):
        str_len = len(string)
        for i in range(int(str_len/2)):
            if string[i] != string[str_len-i-1]:
                return False
        return True

    def solve(self, A):
        if self.is_palindrome(A):
            return 0

        str_len = len(A)
        for i in range(1, str_len):
            if self.is_palindrome(A[:str_len-i]):
                return i

        #required_chars = A[str_len-i:]
        #return required_char[::-1]
        #return len(required_chars)


if __name__ == "__main__":
    print(Solution().solve("AACECAAAA"))
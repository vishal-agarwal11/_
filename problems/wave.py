#Apple will Hire ME
#[0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]
#AeliMpl ilHr Epw e

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        wave = []
        new_text = []
        row = 0
        diff = 1
        for ele in A:
            if row == B - 1:
                diff = -1
            if row == 0:
                diff = 1
            
            wave.append(row)
            try:
                new_text[row] +=ele
            except:
                new_text.append(ele)
            
            row += diff
        print(wave)
        return "".join(new_text)


print(Solution().convert("Apple will Hire ME", 3))

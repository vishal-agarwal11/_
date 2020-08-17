class Solution(object):
    def string_nums_summation(self, string):
        summation = 0
        this_num = ""
        for ele in string:
            try:
                int(ele)
                this_num += ele
            except:
                if len(this_num) != 0:
                    summation += int(this_num)
                    this_num = ""

        if len(this_num) != 0:
            summation += int(this_num)
        return summation


string = "5abc10gfhf5kjdoiw9#1"
print(solution(string))

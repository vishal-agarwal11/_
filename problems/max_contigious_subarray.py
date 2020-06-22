class Solution:
    def maxset(self, A):
        max_value = 0
        ret_val = []
        temp = []
        for ele in A:
            print(temp)
            if ele < 0 and len(temp) > 0 and sum(temp) > max_value:
                max_value = sum(temp)
                ret_val = temp
                temp = []
            elif ele >= 0:
                temp.append(ele)
            
        if len(temp) > 0 and sum(temp) > max_value:
            ret_val = temp
                
        return ret_val

s = Solution()
#print(s.maxset([ 756898537, -1973594324, -2038664370, -184803526, 1424268980 ]))
print(s.maxset([1, 2, 5, -7, 2, 3]))
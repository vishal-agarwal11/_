class Solution:
    # @param A : tuple of integers
    # @return a strings

    def merger(self, A):
        A = [str(ele)  for ele in A]
        A.sort()
        num = A[0]
        for ele in A[1:]:
            if int(num+ele) > int(ele+num):
                num = num + ele
            else:
                num = ele + num
            #print(num)
        return num

    def largestNumber(self, A):
        ds = {}
        s_v = []
        for ele in A:
            f_i = str(ele)[0]
            try:
                ds[int(f_i)].append(str(ele))
            except:
                ds[int(f_i)] = [str(ele)]


        for key in ds:
            if len(ds[key]) == 1:
                s_v.append(ds[key][0])
            else:
                s_v.append(self.merger(ds[key]))
        return self.merger(s_v)


#print(Solution().largestNumber([23, 30, 43, 5, 9]))
#print(Solution().largestNumber([ 472, 663, 964, 722, 485, 852, 635, 4, 368, 676, 319, 412 ]))


ds = {}
ml  = [ 472, 663, 964, 722, 485, 852, 635, 4, 368, 676, 319, 412 ]

for ele in ml:
    f_i = str(ele)[0]
    try:
        ds[int(f_i)].append(str(ele))
    except:
        ds[int(f_i)] = [str(ele)]

s_v = []
for key in ds:
    if len(ds[key]) == 1:
        s_v.append(ds[key][0])
    else:
        s_v.append(Solution().largestNumber(ds[key]))

print(Solution().largestNumber(s_v))
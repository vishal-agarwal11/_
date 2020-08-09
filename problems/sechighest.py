"""
This code return the 1st and 2nd highest in an array
"""

def SecondLargest(x):
        m1=m2=0
        for item in x:
            if item > m1:
               m2 = m1
               m1 = item
            elif m2 < item < m1:
               m2 = item
        return m1, m2

print(SecondLargest([20,67,74,3,2,7,74]))




def getMax2(stones):
    if len(stones) == 2:
        return 0,1 if stones[0] > stones[1] else 1,0
        
    max1=0
    max2=0
    for i in range(len(stones)):
        if stones[i] > stones[max1]:
            max2 = max1
            max1 = i
        if stones[max2] < stones[i] < stones[max1]:
            max2 = i
                
    return max1, max2

print(getMax2([2,7,4,1,8,1]))

"""
Maximum Sequence with negavive numbers
"""

arr = [2, -1,3, -5, 6, -1, 2]
 
def maxSumSequence(arr):
total_max = arr[0]
max_till_here = 0

for i in range(1, len(arr)):
    max_till_here+=arr[i]
    if max_till_here > total_max:
        total_max = max_till_here
    if max_till_here < 0:
        max_till_here = 0
print(total_max)
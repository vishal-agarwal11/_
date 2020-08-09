"""
Given a array of mix of R and B (red and black)
items, it seperates outs the R at start of array
and B at the end of the array.
"""


sample = ["B", "R", "B", "R", "B", "B", "R", "R", "R"]

sample = ["B", "R"]

i = 0
j = len(sample) - 1

while i <= j:
    if sample[i] == "B" and sample[j] == "R":
        sample[i], sample[j] = sample[j], sample[i]
        i+=1
        j-=1
    elif sample[i] == "R" and sample[j] == "R":
        i+=1
    elif sample[i] == "B" and sample[j] == "B":
        j-=1
    elif sample[i] == "R" and sample[j] == "B":
        i+=1
        j-=1
    else:
        print("Never come here")
print(sample)

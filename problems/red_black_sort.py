# Sample Input
#["B", "R", "B", "R", "B", "B", "R", "R", "R"]
#Sample Output
#["R", "R", "R", "R", "R", "B", "B", "B", "B"]


sample = ["B", "R", "B", "R", "B", "B", "R", "R", "R"]

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

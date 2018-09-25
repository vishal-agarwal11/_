import sys
# An efficient search algorithm
# A crude one, could be modified further
# sample - a comma separated input of integers
# search - an element to found in the sample
sample = "2,4,5,6,7,8,11,45,54,66,87,98,102"
search = 67

sample = [int(x) for x in sample.split(",")]

if abs(search-sample[0]) <= abs(search-sample[-1]):
    #start from 0
    init = 0
    while sample[init] <= search:
        print("Iterating forward")
        if sample[init] == search:
            print("Found at index %d" % init)
            sys.exit(0)
        init+=1
else:
    #abs(search-a[0] > abs(search-a[-1]):
    #start from -1
    init = -1
    while sample[init] >= search:
        print("Iterating reverse")
        if sample[init] == search:
            print("Found at index %d" % (len(sample)+init))
            sys.exit(0)
        init+=-1
print("Element %d not found" % search)
def update_k(arr):
    for k in range(len(arr)-1, -1, -1):
        if k+1 != arr[k]:
            return k+1
    #print(f"{f.__qualname__}, {k}")
    return len(arr)


def minimumSwaps(arr):
    swap = 0
    new_end = update_k(arr)
    for i in range(update_k(arr)):
        # the current element is not suppose to be at current
        # scan till last, and check if any element will come 
        # at a place where it is suppose to be
        if arr[i] == i + 1: continue
        if i >= new_end: continue
        for j in range(i+1, new_end):
            if i+1 == arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                swap+=1
                if j+1 == new_end and arr[j] == j+1:
                    new_end = new_end -1
                break
    return swap

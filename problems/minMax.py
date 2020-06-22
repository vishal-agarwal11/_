def sortMinMax(arr):
    min = arr[0]
    max = arr[0]

    for ele in arr:
        if ele < min:
            min = ele
        if ele > max:
            max = ele

    return min,max

        


if __name__ == "__main__":
    arr = [2,4,6,7,1,3,12,15]
    #print(sortMinMax(arr))

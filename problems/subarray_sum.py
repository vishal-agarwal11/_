array = [7, 4, 2, 7, 7, 4 ,1,2, 6, 5, 4, 7, 9, 3,7,1, 6, 6, 5, 8]
r_s = 50

def getarraysum(array, r_s):
    for i in range(len(array)-1):
        sum = array[i]
        for j in range(i+1, len(array)):
            sum +=array[j]
            if sum == r_s:
                return array[i:j+1]

    return -1


print(getarraysum(array, r_s))
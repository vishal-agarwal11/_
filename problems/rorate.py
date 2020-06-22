def rotate(arr):
    rotated = []
    for i in range(len(arr[0])):
        for j in range(len(arr[0])-1, -1, -1):
            rotated.append(arr[j][i])

    return rotated


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
"""
Rotates a matrix to 90 degrees
"""

def rotate(matrix):
    row = len(matrix)
    col = len(matrix[0])

    new_mat = []
    l = 0
    for i in range(col):
        m = col - 1
        temp = []
        for j in range(row):
            temp.append(matrix[m][l])
            m -= 1
        new_mat.append(temp)
        l += 1
    return new_mat


sample1 = [[1,2,3], [4,5,6], [7,8,9]]
sample2 = [[1, 2], [3, 4], [5, 6]]
print(f"Rotated of {sample1} \n{rotate(sample1)}")
print(f"\nRotated of {sample1} \n{rotate(sample2)}")

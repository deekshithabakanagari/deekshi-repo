def max_hourglass(matrix):

    r = len(matrix)
    c = len(matrix[0])

    if r < 3 or c < 3:
        return -1
    
    res = float('-inf')

    for i in range(r - 2):
        for j in range(c - 2):
            temp = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i + 1][j + 1] +  matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
            res = max(res, temp)

    return res

arr = [[1, 2, 3, 0, 0],
       [0, 0, 0, 0, 0],
       [2, 1, 4, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 1, 0, 1, 0]]

print(max_hourglass(arr))
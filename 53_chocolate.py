def choco_dis(arr, m):
    arr.sort()
    result = arr[-1]
    for i in range(len(arr) - m + 1):
        result = min(result, arr[i + m - 1] - arr[i])
    return result

print(choco_dis([7, 3, 2, 4, 9, 12, 56], 3))

# arr = 2 3 4 7 9 12 56
#       ^   ^
def max_diff(arr):
    arr.sort()
    result = 0
    for i in range(1, len(arr)):
        result = max(result, arr[i] - arr[i - 1])
    return result

print(max_diff([3, 6, 9, 1]))

# arr = 1 3 6 9

# result = 0
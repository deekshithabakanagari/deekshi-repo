def max_arr(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        max_val = max(max_val, arr[i])
    return max_val

print(max_arr([23, 45, 82, 27, 66, 12, 78, 13, 71, 86]))

# max_val = 86
def max_arr_idx(arr):
    max_val = arr[0]
    idx = 0
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            idx = i
    return [max_val, idx]

print(max_arr_idx([1, 8, 4, 9, 6]))
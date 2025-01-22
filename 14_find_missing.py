def find_missing(arr):
    n = len(arr) + 1
    actual_sum = n * (n + 1) // 2
    calc_sum = sum(arr)
    return actual_sum - calc_sum

print(find_missing([1, 2, 4, 5, 6]))
def second_largest(arr):
    max1 = max2 = float('-inf')
    for i in arr:
        if i > max1:
            max1, max2 = i, max1
        elif max1 > i > max2:
            max2 = i
    return max2

print(second_largest([1, 3, 5, 2, 4, 6, 8]))
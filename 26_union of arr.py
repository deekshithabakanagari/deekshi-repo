def union_of_sorted_arrays(a, b):
    result = sorted(set(a + b))
    return result
print(union_of_sorted_arrays([1, 2, 3, 4, 5], [1, 2, 3, 6, 7]))

def intersection_of_sorted_arrays(a, b):
    return sorted(list(set(a) & set(b)))
print(intersection_of_sorted_arrays([1, 2, 3, 4, 5], [1, 2, 3, 6, 7]))




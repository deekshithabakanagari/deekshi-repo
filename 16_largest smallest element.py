def largest(arr):
    max_large = float('-inf')
    for i in range(len(arr)):
        if arr[i]>max_large:
            max_large = arr[i]
    return max_large
arr = [10, 89, 9, 56, 4, 80, 8]
print(largest(arr))

def smallest(arr):
    min_small = float('inf')
    for i in range(len(arr)):
        if arr[i]<min_small:
            min_small = arr[i]
    return min_small
arr = [10, 89, 9, 56, 4, 80, 8]
print(smallest(arr))

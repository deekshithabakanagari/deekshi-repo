#largest

def largest(arr):
    largest = 0
    for i in range(len(arr)):
        if arr[i]>largest:
            largest = arr[i]
    return largest

arr = [34,789,67,56,7,0,1000123]
print(largest(arr))


#smallest
def smallest(arr):
    smallest = float("inf")
    for i in range(len(arr)):
        if arr[i]<smallest:
            smallest = arr[i]
    return smallest

arr = [34,789,67,56,7,1000123]
print(smallest(arr))
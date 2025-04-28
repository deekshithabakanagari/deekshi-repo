def missing(arr):
    n = len(arr)
    
    diff = (arr[-1] - arr[0]) // n
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high)//2


        if (arr[mid] - arr[0]) // diff == mid:
            low = mid + 1
        else:
            high = mid - 1

    return arr[high] + diff


arr = [2,26 ]
print(missing(arr))
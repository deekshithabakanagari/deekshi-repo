def elevation_point(arr):
    if len(arr) == 1:
        return arr[0]
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return arr[mid]
        elif arr[mid] < arr[mid - 1]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(elevation_point([1,2,3,4,3,2,1]))
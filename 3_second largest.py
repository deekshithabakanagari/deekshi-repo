def second_largest(arr):
    largest = float('-inf')
    second_largest = float('-inf')
    for  i in range(len(arr)):
        if arr[i]>largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i]>second_largest and arr[i]!=largest:
            second_largest = arr[i]

    return second_largest

arr = [10,20,30,40,50,7]
print(second_largest(arr))

#O(N)
#O(1)
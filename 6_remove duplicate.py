def removeduplicates(arr):
    left = 1
    for right in range(1,len(arr)):
        if arr[right]!=arr[right-1]:
            arr[left] = arr[right]
            left+=1
    return left

arr = [1,1,2,2,2,5,5,4,5,6] 
print(removeduplicates(arr))

#O(N)
#O(1)
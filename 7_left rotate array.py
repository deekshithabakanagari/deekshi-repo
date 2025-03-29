# brute force
# optimised is left rotate array by D places


def leftrotate(arr):
    temp = arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[-1]=temp
    return arr

arr= [11,24,53,64,35]
print(leftrotate(arr))

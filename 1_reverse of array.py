#using while loop

def revofarray(arr):
    left =  0
    right = len(arr)-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left+=1
        right-=1
    return arr
arr = [1,2,3,4,5,6]
print(revofarray(arr))

#using for loop

def revofarray(arr):
    for i in range(len(arr)//2):
        left =  i
        right = len(arr)-i-1
        arr[left],arr[right] = arr[right],arr[left]
    return arr
arr = [1,2,3,4,5,6]
print(revofarray(arr))

tc:o(n)
sc:o(1)
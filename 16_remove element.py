
def removeelement(arr,val):
    left= 0
    right = len(arr)
    while left<right:
        if arr[left] ==  val:
            arr[left] = arr[right-1]
            right-=1
        else:
            left+=1
    return right

arr = [3,2,2,3]
val = 3
print(removeelement(arr,val))

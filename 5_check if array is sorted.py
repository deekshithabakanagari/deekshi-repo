def arraysorted(arr):
    for i in range(1,len(arr)):
        if arr[i]>=arr[i-1]:
            continue
        else:
            return False
    return True

#arr=[4,7,8,9,1,2,3,5,6]
arr = [1,2,2,3,3,4,6,8,76]
print(arraysorted(arr))

def arraysorted(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True

#arr=[4,7,8,9,1,2,3,5,6]
arr = [1,2,2,3,3,4,6,8,76]
print(arraysorted(arr))
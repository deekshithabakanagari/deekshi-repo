# Brute force

def moveallzerostoend(arr):
    temp =[]
    for i in range(len(arr)):
        if arr[i]!=0:
            temp.append(arr[i])

    for i in range(len(temp)):
        arr[i] = temp[i]

    for i in range(len(temp),len(arr)):
        arr[i] = 0
    return arr
arr = [1,2,0,4,0,5,6,0,6,7]
print(moveallzerostoend(arr))
#O(2N)
#O(N)

# optimized
def moveallzerostoendarr(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[pos] = arr[i]
            pos+=1
    while pos < len(arr):
        arr[pos] = 0
        pos+=1

    return arr
arr = [1,2,0,4,0,5,6,0,6,7]
print(moveallzerostoendarr(arr))
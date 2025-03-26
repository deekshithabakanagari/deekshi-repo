def linear_search(arr,num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1
arr = [1,2,3,4,0]
num = 3
print(linear_search(arr,num))
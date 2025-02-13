def mov_neg_to_end(n):
    left = 0
    for right in range(len(n)):
        if n[left]<0 and n[right]>0:
            n[left],n[right] = n[right],n[left]
        if n[left]>0:
            left+=1

n=[1,-1,2,-3,6,-7,-9,-10]
mov_neg(n)
print(n)


def mov_neg_to_start(n):
    left = 0
    for right in range(len(n)):
        if n[left]>0 and n[right]<0:
            n[left],n[right] = n[right],n[left]
        if n[left]<0:
            left+=1

n=[1,-1,2,-3,6,-7,-9,-10]
mov_neg_to_start(n)
print(n)


# # tc:o(n)
# # sc:o(1)


def move_zeros_to_end(arr):
    left = 0
    for right in range(1, len(arr)):
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[left] != 0:
            left += 1
arr=[0,1,0,3,12]
move_zeros_to_end(arr)
print(arr)


def move_zeros_to_start(arr):
    left = 0
    for right in range(1, len(arr)):
        if arr[left] != 0 and arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[left] == 0:
            left += 1
arr=[0,1,0,3,12,0,4,0]
move_zeros_to_start(arr)
print(arr)
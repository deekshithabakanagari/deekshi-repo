#Not Done
# brute force
# max interger which on squaring <= n:

def sqrtroot(n):
    ans = 1
    for i in range(n+1):
        if i*i <= n:
            ans = i
    return ans
n = 8

print(sqrtroot(n))


def binary_search(arr, target):
    low, high = 0, len(arr) - 1  
    
    while low <= high:
        mid = (low + high) // 2  
        if arr[mid*mid] <= target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1  
        else:
            high = mid - 1  
    
    return -1  # Target not found
arr = []

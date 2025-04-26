def sumofdigits(arr):
    m = float('inf')
    for i in range(1,len(arr)):
        if arr[i] < m:
            m = arr[i]

    n = m
    sum  = 0
    while n!=0:
        d = n%10
        sum = sum + d
        n = n//10

    if sum%2 == 0:
        return True
    return False


arr = [444,555,333,222]
print(sumofdigits(arr))
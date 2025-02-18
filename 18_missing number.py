def missingnumber(arr,n):
    total_sum = sum(arr)
    exp_sum = n*(n+1)//2
    return exp_sum - total_sum

arr = [1,2,4,6,3,7,8]
n = 8
print(missingnumber(arr,n))
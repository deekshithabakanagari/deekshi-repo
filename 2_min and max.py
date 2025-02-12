def minmax(arr):
    max_val = float('-inf')
    min_val = float('inf')
    for i in arr:
        if i > max_val:
            max_val = i
        elif i < min_val:
            min_val = i
    return max_val,min_val

arr=[22,3,4,5,77,-1,4]
print(minmax(arr))

tc:o(n)
sc:o(1)
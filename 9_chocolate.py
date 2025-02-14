def chocolate(arr,m):
    arr.sort()
    result = float('inf')
    for i in range(len(arr)-m+1):
        curr = arr[i+m-1]-arr[i]
        result = min(result,curr)
    return result

arr= [3, 4, 1, 9, 56, 7, 9, 12]
m=5
print(chocolate(arr,m))

tc:o(nlogn)
sc:o(1)
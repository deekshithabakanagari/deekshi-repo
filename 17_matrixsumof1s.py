def rowWithMax1s(arr):
    # code here
    count=0
    cmax=0
    for i in range(len(arr)):
        count=sum(arr[i])
        if count>cmax:
            cmax=count
            r=i
    return r

arr=[[1,1,1,1], [0,0,1,1], [1,1,0,1], [0,0,0,0]]
print(rowWithMax1s(arr))

tc:O(m*n)
sc:O(1)
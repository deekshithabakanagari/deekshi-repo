def sort012(arr):
    count = [0,0,0]
    for i in arr:
        count[i]+=1
    a,b,c = count
    arr[:a] = [0]*a
    arr[a:a+b] = [1]*b
    arr[a+b:] = [2]*c
    
arr=[0, 1, 2, 0, 1, 2]  
sort012(arr)
print(arr)  

tc:o(n)
sc:o(1)

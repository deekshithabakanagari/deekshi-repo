# direct optimal approach
def maxconsecutiveones(arr):
    maxi = 0
    count = 0
    for  i in range(len(arr)):
        if arr[i] == 1:
            count+=1
            maxi = max(maxi,count)
        else:
            count = 0
    return maxi

arr = [1,0,1,1,0,1]
print(maxconsecutiveones(arr))
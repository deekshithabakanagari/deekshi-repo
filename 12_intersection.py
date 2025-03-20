#brute force
def intersection(arr1,arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    intersection = list(set1.intersection(set2))
    return sorted(intersection)

arr1  = [1,2,2,3,4]
arr2  = [2,2,3,5]
print(intersection(arr1,arr2))


#optimised
def intersectionofarray(a,b):
    n = len(a)
    m = len(b)
    i,j = 0,0
    ans = []
    while i<n and j<m:
        if a[i] == b[j]:
            if len(ans)==0 or ans[-1]!=a[i]:
                ans.append(a[i])
            i+=1
            j+=1
        elif a[i] < b[j]:
            i+=1
        else:
            j+=1
    return ans

a  = [1,2,2,3,4]
b  = [2,2,3,5]
print(intersectionofarray(a,b))

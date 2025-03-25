# Brute force

def unionofarray(arr1,arr2):
    set1  = set(arr1)
    set2  = set(arr2)
    union_set = set1.union(set2)
    result = sorted(union_set)
    return result

arr1 =[1,1,1,1,1]
arr2 = [2,2,2,2,2]
print(unionofarray(arr1,arr2))

#optimized solution
def findUnion(a,b):
        n = len(a)
        m = len(b)
        i,j = 0,0
        ans = []

        
        while i<n and j<m:
            if a[i]<=b[j]:
                if len(ans)==0 or ans[-1]!=a[i]:
                    ans.append(a[i])
                i+=1
            else:
                if len(ans)==0 or ans[-1]!=b[j]:
                    ans.append(b[j])
                j+=1



        while i<n:
            if len(ans)==0 or ans[-1]!=a[i]:
                ans.append(a[i])
            i+=1    

        while j<m:
            if len(ans)==0 or ans[-1]!=b[j]:
                ans.append(b[j])
            j+=1

        return ans          
             
a = [1,2,3,4,5]
b = [1,2,3]
print(findUnion(a,b))
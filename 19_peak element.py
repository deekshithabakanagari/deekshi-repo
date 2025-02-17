def peakelement(n):
    n=[float('-inf')] + n + [float('-inf')]
    for i in range(1,len(n)-1):
        if n[i]>n[i-1]  and n[i]>n[i+1]:
            return i - 1
n = [1,2,4,5,7,8,3]
print(peakelement(n))






#use binary search
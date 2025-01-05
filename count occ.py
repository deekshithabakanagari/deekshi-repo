def count_occ(l,n):
    count = 0
    for i in l:
        if i==n:
            count+=1
    return count
l=[23,45,23,67]
n=23
print(count_occ(l,n))



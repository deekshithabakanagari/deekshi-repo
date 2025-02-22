def union(n1,n2):
    hashset = set()
    for i in n1:
        hashset.add(i)
    for i in n2:
        hashset.add(i)
    return len(hashset)

n1=[1,2,3,4,5]
n2=[1,2,4]
print(union(n1,n2))

tc:o(n+m)
sc:o(n+m)

#this union program returns length 
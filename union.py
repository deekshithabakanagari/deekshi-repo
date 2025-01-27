#union of 2 lists
def union(l1,l2):
    for i in l2:
        if i not in l1:
            l1.append(i)
    return l1
l1=[1, 2, 3, 4, 5, 6]
l2=[2, 4, 6, 8, 10, 12]
print(union(l1,l2))

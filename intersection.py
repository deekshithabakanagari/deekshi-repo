def intersection(l1, l2):
    hashmap = dict()
    for i in l1:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    result = []
    for i in l2:
        if i in hashmap and hashmap[i]!=0:
            result.append(i)
            hashmap[i]-= 1
    return result

#intersection
def intersection(l1,l2):
    result =[]
    for i in l2:
        if i in l1:
            result.append(i)
    return result
l1=[1, 2, 3, 4, 5, 6]
l2=[2, 4, 6, 8, 10, 12]
print(intersection(l1,l2))
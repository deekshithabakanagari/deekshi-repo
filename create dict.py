def dictinary(L):

    d = {}
    for i in range(len(L)):
        if L[i][0] in D:
            d[L[i][0]].append(L[i][1])
        else:
            D[L[i][0]]=[]
            d[L[i][0]].append(L[i][1])

L=[['a', 1], ['b', 2], ['a', 3], ['c', 4]] 
print(dictinary(L))

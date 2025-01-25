def odd(l):
    hashmap = dict()
    for i in l:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1
    for i in hashmap:
        if hashmap[i]%2==1:
            return i

l=[1,2,3,1,2,3,4,1,2,3,1,2,4,3,4]
print(odd(l))
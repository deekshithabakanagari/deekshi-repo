def swap(l):
    l[0],l[-1]=l[-1],l[0]
    return l
l=[23,45,67,89]
print(swap(l))
def remove_dup(l):
    left = 1
    for right in range(1,len(l)):
        if l[left-1]!=l[right]:
            l[left]=l[right]
            left+=1
    return l[:left]
l=[10,20,20,30,40,40,50]
print(remove_dup(l))
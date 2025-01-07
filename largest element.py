def largest_element(l):
    result=0
    for i in range(len(l)):
        if l[i]>result:
           result = l[i]
    
    return result

l=[11,22,55,78,41,156]
print(largest_element(l))
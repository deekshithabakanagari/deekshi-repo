def secondlargest(l):
    max1 = max2 = float ('-inf')
    for i in l:
        if i>max1:
            max1,max2 = i,max1
        elif max1>i>max2:
            max2 = i
    return max2
l=[4,5,6,7,8,9,12]
print(secondlargest(l))
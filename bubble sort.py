def bubblesort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j][1] > l[j+1][1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l
l=[[['akash', 5], ['rishav', 10], ['gaurav', 15], ['ram', 20]]]
print(bubblesort(l))
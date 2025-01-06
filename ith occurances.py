def cummulative_sum(l):
    cumm = [l[0]]
    for i in range(1,len(l)):
        cumm.append(cumm[-1]+l[i])
    return cumm
l=[1,2,3,4,5]
print(cummulative_sum(l))       
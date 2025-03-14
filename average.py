def average(l):
    total = 0
    length = 0
    for i in l:
        total+=i
        length+=1
    avg = total/length
    return round(avg,2)

l=list(map(int,input().split()))
print(average(l))
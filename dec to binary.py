n = int(input())
result = []
while n!=0:
    d = n%2
    result.append(d)
    n = n//2
    print(result)
result.reverse()
for i in result:
    print(i,end="")

#12--------->1100
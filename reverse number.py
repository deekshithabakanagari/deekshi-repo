n = int(input())
rev = 0
while(n>0):
    m=n%10
    rev = rev*10+m
    n=n//10
print(rev)

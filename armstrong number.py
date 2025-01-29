n = int(input())
order = len(str(n))
temp = n
sum = 0

while n:
    m=n%10
    sum+=m**order
    n=n//10 

if temp == sum:
    print("armstrong")
else:
    print("not armstrong")



#b function approach
def armstrong(n):
    sum = 0
    order = len(str(n))
    while n:
        m=n%10
        sum+=m**order
        n//=10
    return sum
n=int(input())
if armstrong(n) == n:
    print("armstrong")
else:
    print("not armstrong")

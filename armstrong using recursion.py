def is_armstrong(n,order,sum=0):
    
    if n == 0:
        return sum
    else:
        m=n%10
        sum+=m**order
        return is_armstrong(n//10,order,sum)

n = int(input())
if is_armstrong(n,len(str(n)))==n:
    print("armstrong")
else:
    print("Not armstrong")
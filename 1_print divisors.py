# n = int(input())
# i =1
# while(n!=0):
#     if(n%i==0):
#         print(i)
#     i+=1
    

def print_divisors(n):
    divisors = []

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)  
            if i != n // i: 
                divisors.append(n // i)
    
    divisors.sort()

    for divisor in divisors:
        print(divisor,end=" ")

n = 36
print_divisors(n)

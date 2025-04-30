# def evennumber(number):

#     for i in range(1,number + 1):
#         if i%2 == 0 :
#             print(i,end=" ")
       


# number = 16
# evennumber(number)


#multiplication table

# def multiplicationtable(number):

#     for i in range(1,11):
#         print( number, "*" ,i ,"=", number*i)

# number = 5
# multiplicationtable(number)

#sumof natural numbers

# def solve(n):
#     sum = 0
#     for i in range(n+1):
#         sum += i
#     return sum
# n = 5
# print(solve(n))

#swap two numbers

# def swaptwonumbers(n1,n2):
#         temp = n1
#         n1 = n2
#         n2 = temp
#         return n1 ,n2

# n1 = 20
# n2 = 78
# print(swaptwonumbers(n1,n2))


# closest number



def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if num % i == 0:
            return False
    return True

def closest_prime(n):
    lower = n
    upper = n

    # Look for the nearest primes both downward and upward
    while not is_prime(lower):
        lower -= 1
    while not is_prime(upper):
        upper += 1

    # Return the closer prime (or the lower one in case of tie)
    if abs(n - lower) <= abs(n - upper):
        return lower
    else:
        return upper

# Example usage:
n = 95

print(closest_prime(n))

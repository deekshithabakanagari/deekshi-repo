#1st approach 
n = int(input())
if n & 1:
    print('odd')
else:
    print('even')


#2nd approach using recursion
def check(n):
    if (n<2):
        return n%2 == 0
    return check(n-2)
n=int(input())
if check(n) == True:
    print('even')
else:
    print('odd')

#3rd approach using lamda
n = int(input())
n1 = lambda n: "even" if n%2 == 0 else "odd"
print(n1(n))


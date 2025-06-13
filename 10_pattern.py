#hallow hour glass 

n = 5

for i in range(n-1):
    for j in range(i):
        print(" ",end="")

    for j in range(n-i):
        if j==0 or j ==n-i-1 or i== 0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
n = 5

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i + 1):
        if j == 0 or j == i or i == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
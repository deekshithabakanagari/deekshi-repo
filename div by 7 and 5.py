def div(L,u):
    for i in range(L,u+1):
        if(i%7==0 and i%5==0):
            print(i)
L=int(input())
u=int(input())
div(L,u)
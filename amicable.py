x = int(input())
y = int(input())
sum1,sum2 = 0,0
for i in range(1,x):
    if(x%i==0):
        sum1+=i
for j in range(1,y):
    if(y%j==0):
        sum2+=j
if (sum1==y and sum2==x):
    print("amicable")
else:
    print("Not amicable")

import random
def ran(l):
    result=[]
    for i in range(l):
        result.append(random.randint(1,20))
    return result
l=int(input())
print(ran(l))
    
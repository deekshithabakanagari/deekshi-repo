def bin_dec(n):
    result= 0
    power = 1
    while n:
        result+=n%10*power
        n//=10
        power*=2
    return result

n=int(input())
print(bin_dec(n))

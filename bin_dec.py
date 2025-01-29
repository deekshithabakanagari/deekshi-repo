def dec_bin(n):
    result=0
    div = 1
    while n:
        result+=(n%2)*div
        n//=2
        div*=10
    return result
n=int(input())
print(dec_bin(n))

def fib(n,hashmap=dict()):
    if n in hashmap:
        return hashmap[n]
    if n<=1:
        return n
    hashmap[n] = fib(n-1)+fib(n-2)
    return hashmap[n]
n=4
print(fib(n,hashmap=dict()))
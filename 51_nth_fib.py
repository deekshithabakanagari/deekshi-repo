def nth_fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    first = 0
    second = 1
    for i in range(n):
        cur = first + second
        first, second = cur, first

    return first

print(nth_fib(9))
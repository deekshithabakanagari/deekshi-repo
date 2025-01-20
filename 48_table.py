def table(n):
    result = 0
    for i in range(1, 11):
        print(n * i, end=' ')
        result += n * i
    print()
    print(result)

table(12)
def sum35(n1, n2):
    result = 0
    for i in range(n1, n2 + 1):
        if i % 3 == 0 and i % 5 == 0:
            result += i
    return result

print(sum35(12, 50))
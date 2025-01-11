def even_odd(arr):
    result = ''
    for i in arr:
        if i % 2:
            result += 'odd '
        else:
            result += 'even '
    return result

print(even_odd([1, 2, 3, 4, 5, 6]))
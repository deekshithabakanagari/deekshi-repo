def replace(s, c1, c2):
    result = ''
    for i in s:
        if i == c1:
            result += c2
        elif i == c2:
            result += c1
        else:
            result += i
    return result

print(replace('apples', 'a', 'p'))

# result = 'paales'
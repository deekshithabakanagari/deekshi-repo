def string_rev(s):
    result = ''
    for i in s:
        result = i + result
    return result

print(string_rev('hello'))
def string_decode(num):
    num = str(num)
    result = ''
    count = 0
    for i in num:
        if i == '1':
            count += 1
        else:
            result += chr(count + 64)
            count = 0
    result += chr(count + 64)
    return result

print(string_decode(10110111))

# 10110111
#        ^
# count = 3
# result = 'ABC'
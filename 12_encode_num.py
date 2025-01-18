def encode_num(num):
    result = ''
    while num:
        result = str((num % 10) ** 2) + result
        num //= 10
    return int(result)

print(encode_num(34))
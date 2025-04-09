def dec_bin(num):
    result = ''
    while num:
        result = str(num % 2) + result
        num //= 2
    return result

print(dec_bin(8))
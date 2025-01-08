def binary_ops(s):
    result = int(s[0])
    ptr = 1
    while ptr < len(s):
        if s[ptr] == 'A':
            result = result & int(s[ptr + 1])
        elif s[ptr] == 'B':
            result = result | int(s[ptr + 1])
        elif s[ptr] == 'C':
            result = result ^ int(s[ptr + 1])
        ptr += 2
    return result

print(binary_ops('0C1A1B1C1C1B0A0'))
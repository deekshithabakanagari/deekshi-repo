def move_hyphen(s):
    hyphen_count = 0
    for i in s:
        if i == '-':
            hyphen_count += 1
    result = '-' * hyphen_count
    for i in s:
        if i != '-':
            result += i
    return result

print(move_hyphen('Move-hyphens-to-front'))
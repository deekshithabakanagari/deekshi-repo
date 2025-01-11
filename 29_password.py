def strong_password(password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+ "
    result = 4
    num = low = upp = spc = False
    for i in password:
        if i in numbers:
            num = True
        elif i in lower_case:
            low = True
        elif i in upper_case:
            upp = True
        elif i in special_characters:
            spc = True
    if num:
        result -=1
    if low:
        result -= 1
    if upp:
        result -= 1
    if spc:
        result -= 1
    return max(6 - len(password), result)

print(strong_password('a987 abC012'))
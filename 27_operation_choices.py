def op_choices(c, a, b):
    if c == 1:
        return a + b
    if c == 2:
        return a - b
    if c == 3:
        return a * b
    if c == 4:
        return a / b
    
print(op_choices(2, 16, 20))
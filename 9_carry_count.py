def carry_count(n1, n2):
    result = 0
    carry = 0
    n_sum = 0
    while n1 or n2:
        cur = 0
        if n1:
            cur += n1 % 10
            n1 //= 10
        if n2:
            cur += n2 % 10
            n2 //= 10
        cur += carry
        n_sum += cur % 10
        carry = cur // 10
        if carry:
            result += 1
    return result

print(carry_count(23, 563))
# -
# 4 5 1     cur = 10
# 3 4 9
# 8 0 0
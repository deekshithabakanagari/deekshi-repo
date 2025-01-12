def rearrangement(n):

    # Decimal to binary
    def dec_bin(num):
        result = ''
        while num:
            result = str(num % 2) + result
            num //= 2
        return result
    
    binary = dec_bin(n)
    rearranged_binary = int('1' * binary.count('1'))

    # Binary to decimal
    def bin_dec(num):
        result = 0
        power = 1
        while num:
            result += (num % 10) * power
            num //= 10
            power *= 2
        return result
    
    return bin_dec(rearranged_binary)

print(rearrangement(2))
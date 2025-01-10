def neg_price(arr):
    result = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            result += 1
    return result

print(neg_price([6]))
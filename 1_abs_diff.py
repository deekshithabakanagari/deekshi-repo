def absDiff(arr, length, num, diff):
    count = 0
    for i in arr:
        if abs(num - i) <= diff:
            count += 1
    return count

arr = [12, 3, 14, 56, 77, 13]
num = 13
diff = 2
length = 6

print(absDiff(arr, length, num, diff))
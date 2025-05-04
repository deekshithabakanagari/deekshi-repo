def largestOddNumber(self, num: str) -> str:
    idx = 0
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2:
            idx = i
            break
    else:
        return ''
    return num[:idx + 1]

# Time - O(N)
# Space - O(1)
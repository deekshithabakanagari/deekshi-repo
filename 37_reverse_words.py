def rev_words(s):
    s_arr = s.split()
    left = 0
    right = len(s_arr) - 1
    while left < right:
        s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
        left += 1
        right -= 1
    return ' '.join(s_arr)

print(rev_words('Hello World'))

# arr = ['World', 'Hello']
#         L           R
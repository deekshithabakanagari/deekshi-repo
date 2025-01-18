def first_k(s, k):
    res = ''
    for i in s:
        if i == ' ':
            k -= 1
        res += i
        if not k:
            return res
        
print(first_k('Hello I am a passionate developer', 4))
def replace_freq(s, t):
    hashmap = dict()
    for i in s:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    max_char = ''
    count = 0
    for i in s:
        if hashmap[i] > count:
            max_char = i
            count = hashmap[i]
    return s.replace(max_char, t)

print(replace_freq('bbadbbababb', 't'))

# hashmap = {'b': 7, 'a': 3, 'd': 1}
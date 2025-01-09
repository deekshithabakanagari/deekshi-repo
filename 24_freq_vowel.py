def freq_vowel(s):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for i in s:
        if i in {'a', 'e', 'i', 'o', 'u'}:
            vowels[i] += 1
    result = ''
    count = 0
    for i in 'aeiou':
        if vowels[i] > count:
            result = i
            count = vowels[i]
    return result

print(freq_vowel('xayuaba'))

# vowels = {'a': 2, 'e': 0, 'i': 0, 'o': 0, 'u': 4}

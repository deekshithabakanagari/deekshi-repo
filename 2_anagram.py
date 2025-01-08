def anagram(s, t):
    
    if len(s) != len(t):
        return 'Not Anagram'
    
    s_map = dict()
    for i in s:
        if i in s_map:
            s_map[i] += 1
        else:
            s_map[i] = 1

    t_map = dict()
    for i in t:
        if i in t_map:
            t_map[i] += 1
        else:
            t_map[i] = 1

    return 'Anagram' if s_map == t_map else 'Not Anagaram'


    # s = 'anagram'
    # t = 'nagaramt'
    # s_map = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
    # t_map = {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}

print(anagram('listen', 'sient'))
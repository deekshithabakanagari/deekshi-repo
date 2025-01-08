def auto_num(n):
    n_str = str(n)
    count = [0] * 10
    for i in n_str:
        count[int(i)] += 1
    for i in range(len(n_str)):
        if int(n_str[i]) != count[i]:
            return 0
    return len(set(n_str))

print(auto_num(1210))

# count = 1 2 1 0 0 0 0 0 0 0 
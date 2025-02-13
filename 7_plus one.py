def plusone(n):
    n = n[::-1]
    c = 1
    for i in range(len(n)):
        if n[i] + c < 10:
            n[i] += c
            c = 0
            break
        else:
            n[i]=0
    if c:
        n.append(c)
    return n[::-1]

n=[1,2,5]
print(plusone(n))

tc:o(n)
sc:o(1)
def findPattern(stream, pattern):

    for i in range(len(stream) - len(pattern) + 1):
        sub = stream[i:i + len(pattern)]
        if sub == pattern:
            return i
        
    return -1

stream = [1, 1, 1, 0, 1, 1, 1]
pattern = [0, 1]
print(findPattern(stream, pattern))
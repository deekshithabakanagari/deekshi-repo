def intersection(arr1, arr2):
    hashmap = dict()
    for i in arr1:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    result = []
    for i in arr2:
        if i in hashmap and hashmap[i]:
            result.append(i)
            hashmap[i] -= 1
    return result

print(intersection([1, 2, 2, 3, 4], [2, 2, 2, 3, 5]))

# hashmap = {1: 1, 2: 0, 3: 0, 4: 1}
# result = [2, 2, 3]
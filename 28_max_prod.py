def max_prod(arr, target):
    prod = 0
    result = None
    hashmap = dict()
    for i in range(len(arr)):
        if target - arr[i] in hashmap:
            if arr[i] * (target - arr[i]) > prod:
                result = [arr[i], target - arr[i]]
                prod = arr[i] * (target - arr[i])
        else:
            hashmap[arr[i]] = i
    return result

print(max_prod([11,1,2,8,10,11,15,7], 18))

# hashmap = {11: 0, 1: 1, 2: 2, 8: 3, 11: 5}
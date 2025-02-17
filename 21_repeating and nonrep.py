#non-repeating

def non_repeat(nums):
    hashmap = dict()
    for i in nums:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    for i in nums:
        if hashmap[i] == 1:
            return i
    return 0

nums = [-1, 2, -1, 3, 2]
print(non_repeat(nums))


#repeating
def repeat(nums):
    hashmap = dict()
    for i in nums:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    for i in nums:
        if hashmap[i] != 1:
            return i
    return 0

nums = [-1, 2, -1, 3, 2]
print(repeat(nums))
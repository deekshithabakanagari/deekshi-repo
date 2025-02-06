def twoSum(nums,target):
    hashmap ={}
    for i,num in enumerate(nums):
        if target - num in hashmap:
            return[i,hashmap[target - num]]
        hashmap[num]=i

    

print(twoSum([2,7,11,15], target = 9))

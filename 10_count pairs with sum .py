def count_pairs_with_given_sum(arr, target):
    count = 0
    hashmap = dict()
    
    for num in arr:
        i = target - num
        if i in hashmap:
            count += hashmap[i]  
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
            
    return count

arr = [10,12,10,15,-1]
target = 20
print(count_pairs_with_given_sum(arr, target))  
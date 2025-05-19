class Solution:
    def sumOfUnique(self, nums) -> int:
        
        # Declaring variables
        hashmap = dict()
        res = 0

        # Iterating over nums
        for i in nums:
            if i in hashmap:
                if hashmap[i]:
                    res -= i
                    hashmap[i] -= 1
            else:
                res += i
                hashmap[i] = 1

        # Returning the result
        return res
    
# Time - O(N)
# Space - O(N)
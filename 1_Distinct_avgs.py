class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        
        # Sorting nums and declaring variables
        nums.sort()
        hashset = set()
        l = 0
        r = len(nums) - 1

        # Iterating over nums
        while l < r:
            hashset.add((nums[l] + nums[r]) / 2)
            l += 1
            r -= 1

        # Returning the result
        return len(hashset)

# Time - O(N logN)
# Space - O(N)
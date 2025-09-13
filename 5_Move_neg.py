# This code is used to move all the negative numbers to the right of the array

def move_neg(nums):
    left = 0
    for right in range(1, len(nums)):
        if nums[left] < 0 and nums[right] >= 0:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] > 0:
            left += 1
        
nums = list(map(int, input('Enter space separated nums: ').split()))
move_neg(nums)
print(nums)

# Time Complexity = O(n)
# Space Complexity = O(1)

# Left         L
# nums    1 3 -1 2 -7 -5 11 6
# Right             R
# This code is used to reverse an array

# Using while loop
def reverse(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums

# Using for loop
def reverse_f(nums):
    for i in range(len(nums) // 2):
        left = i
        right = len(nums) - i - 1
        nums[left], nums[right] = nums[right], nums[left]
    return nums

nums = list(map(int, input('Enter space separated nums: ').split()))
# print(reverse(nums))
print(reverse_f(nums))

# Time Complexity = O(n)
# Space Complexity = O(1)
# These are same for both for and while loops
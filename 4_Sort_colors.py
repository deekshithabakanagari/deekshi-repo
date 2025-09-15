# Need to watch neetcode video for a one pass O(n) solution

# Bucket sort / Counting sort solution
def sort_colors1(nums):
    counts = [0, 0, 0]
    for i in nums:
        counts[i] += 1
    r, w, b = counts
    nums[:r] = [0] * r
    nums[r:r + w] = [1] * w
    nums[r + w:] = [2] * b

# My approach using a two pass solution
def two_pass(nums):
    # Moving zeroes to the left
    left = 0
    for right in range(1, len(nums)):
        if nums[left] != 0 and nums[right] == 0:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] == 0:
            left += 1
    # Moving twos to the right
    left = 0
    for right in range(1, len(nums)):
        if nums[left] == 2 and nums[right] != 2:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] != 2:
            left += 1

# Neetcode approach using one pass
def one_pass(nums):
    left, right = 0, len(nums) - 1
    i = 0
    while i <= right:
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
            i -= 1
        i += 1

nums = list(map(int, input('Enter space separated nums: ').split()))
# sort_colors1(nums)
# two_pass(nums)
one_pass(nums)
print(nums)

# Time Complexity = O(n)
# Space Complexity = O(1)
# This is the same for all the three approaches
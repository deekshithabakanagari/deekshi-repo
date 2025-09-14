# This code is used to rotate the array by 1

def rotate(nums):
    temp = nums.pop()  #
    nums.insert(0, temp)

nums = list(map(int, input('Enter space separated nums: ').split()))
rotate(nums)
print(nums)

# Time Complexity = O(n)
# Space Complexity = O(1)
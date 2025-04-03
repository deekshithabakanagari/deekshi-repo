# # brute force

# def missingnumber(arr):
#     for i in range(1,len(arr)+1):
#         flag =0
#         for j in range(0,len(arr)-1):
#             if arr[j]== i:
#                 flag=1
#                 break
#     if flag == 0:
#         return i
        
# arr = [1,2,3,5]
# # arr = [1,2,4,3] does not work for this
# print(missingnumber(arr))

# #optimal solution
# # by hashing
# def missingnumber(arr,n):
#     hash_table = [0]*(n+1)

#     for num in arr:
#         hash_table[num] = 1

#     for i in range(1,n+1):
#         if hash_table[i]==0:
#             return i
    
# arr = [9,6,4,2,3,5,7,0,1]
# n = 9
# print(missingnumber(arr,n))
# #O(n)
# #O(n)


# def missingNumber(arr):
#     n = len(arr)+1
#     actual_sum = n*(n+1)//2
#     expected_sum = sum(arr)
#     result = actual_sum - expected_sum
    
#     return result
# arr = [1,2,3,4,5,7,8]
# n = 8
# print(missingNumber(arr))

# # most optimal solution
# def xorofarrays(arr):
#     xor1 = 0
#     xor2 = 0
#     for i in range(len(arr)+1):
#         xor1 ^= i

#     for num in arr:
#         xor2 ^= num
        
#     return xor1 ^ xor2

# arr = [3,0,1]
# print(xorofarrays(arr))


# O(N)
# O(1)
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Binary search for the missing number
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > mid:
                high = mid
            else:
                low = mid + 1
        
        return low

# Example usage:
solution = Solution()
nums = [9,6,4,2,3,5,7,0,1]  # Array with missing number
print(solution.missingNumber(nums))  # Output: 2

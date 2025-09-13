# This code is used to get the no. of elements in the union of two arrays

def union_count(nums1, nums2):
    hashset = set()
    for i in nums1:
        hashset.add(i)
    for i in nums2:
        hashset.add(i)
    return len(hashset)

nums1 = list(map(int, input('Enter set 1 elements: ').split()))
nums2 = list(map(int, input('Enter set 2 elements: ').split()))
print(union_count(nums1, nums2))

# Time complexity: O(n + m)
# Space complexity: O(n + m)
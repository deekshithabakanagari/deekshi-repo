class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # Declaring variables
        h = len(haystack)
        n = len(needle)

        # Iterating over the haystack
        for i in range(h - n + 1):
            if needle == haystack[i:i + n]:
                return i

        return -1
    
# Time - O(N)
# Space - O(1)
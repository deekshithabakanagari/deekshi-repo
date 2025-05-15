class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Declaring variables
        first = 0
        second = 1

        # Iterating to get the result
        for i in range(n):
            temp = first + second
            first, second = second, temp

        # Returning the result
        return second
    
# Time - O(N)
# Space - O(1)
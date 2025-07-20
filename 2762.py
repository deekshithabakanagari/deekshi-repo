def continuousSubarrays(nums):
        
        count = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                
                sub = nums[i:j + 1]
                if max(sub) - min(sub) <= 2:
                    count += 1

        return count

nums = [1, 2, 3]
print(continuousSubarrays(nums))
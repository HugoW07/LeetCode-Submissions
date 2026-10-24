class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        
        for i, n in enumerate(nums):
            needed = target - n

            if needed in seen:
                return seen[needed],i 
            
            if n not in seen:
                seen[n] = i    

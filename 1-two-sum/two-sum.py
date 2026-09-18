class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        
        for i,n in enumerate(nums):
            diff = target - n

            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
            
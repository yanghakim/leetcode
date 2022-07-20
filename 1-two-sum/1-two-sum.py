class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        holder = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in holder:
                return [holder[complement], i]
            
            holder[nums[i]] = i
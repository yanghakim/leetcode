class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum = 0
        rightSum = sum(nums)
        
        
        for (index, item) in enumerate(nums):
            if (leftSum == rightSum - leftSum - item):
                return index
            leftSum += item
        return -1
                
        
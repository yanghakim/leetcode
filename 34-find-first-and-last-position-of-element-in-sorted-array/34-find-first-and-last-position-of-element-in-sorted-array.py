class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # get leftmost index
        res = [-1, -1]
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
                res[0] = mid
                res[1] = mid
            elif target < nums[mid]:
                right = mid
            else:
                left = mid + 1
           
        # if none, return res
        if res[0] == -1:
            return res
        
        # start from left index
        left = res[0] + 1
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
                res[1] = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
                
        return res
    
                
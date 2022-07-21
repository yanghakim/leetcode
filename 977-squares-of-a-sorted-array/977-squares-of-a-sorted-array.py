class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [None] * length
        insert_index = length - 1
        left = 0
        right = length - 1
        
        while (left <= right):
            if abs(nums[left]) < abs(nums[right]):
                result[insert_index] = nums[right] ** 2
                right -= 1
            else:
                result[insert_index] = nums[left] ** 2
                left += 1
            insert_index -= 1

            
        return result
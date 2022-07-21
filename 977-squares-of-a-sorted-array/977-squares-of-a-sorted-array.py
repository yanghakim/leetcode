class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squaredNums = [num ** 2 for num in nums]
        
        return list(sorted(squaredNums))
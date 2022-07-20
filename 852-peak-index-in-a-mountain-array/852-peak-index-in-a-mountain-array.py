class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if (len(arr) < 3):
            return False
        left, right = 0, len(arr)
        
        while (left < right):
            middle = left + (right - left) // 2
            
            if arr[middle] < arr[middle + 1]:
                left = middle + 1
            else: 
                right = middle
        return left
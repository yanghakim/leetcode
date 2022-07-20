class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        ans=arr.index(max(arr))
        
        return ans
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak = arr.index(max(arr))
        return peak
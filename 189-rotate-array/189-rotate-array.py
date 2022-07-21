class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import deque
        k = k % len(nums)
        i = 0
        d = deque(nums)
        while i < k:
            temp = d.pop()
            d.appendleft(temp)
            i += 1
        nums[:] = d
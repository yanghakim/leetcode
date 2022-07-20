class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        passed = set()
        for x in nums:
            if x in passed:
                return True
            passed.add(x)
        return False
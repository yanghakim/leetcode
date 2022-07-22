class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        holder = set()
        
        for x in nums:
            if (x in holder):
                return True
            else:
                holder.add(x)
        return False
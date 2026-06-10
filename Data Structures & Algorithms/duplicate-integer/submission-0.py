class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()

        for i in nums:
            if i not in dup:
                dup.add(i)
            elif i in dup:
                return True
        
        return False
        
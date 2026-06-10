class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        o = 0
        for i in nums:
            if i in seen:
                o = i
            elif i not in seen:
                seen.add(i)
        
        return o
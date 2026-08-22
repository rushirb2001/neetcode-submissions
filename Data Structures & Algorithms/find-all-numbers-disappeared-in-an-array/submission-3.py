class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = set(nums)

        res = []

        for i in range(1, n+1):
            if i not in d:
                res.append(i)
            
        return res
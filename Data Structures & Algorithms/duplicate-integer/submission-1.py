class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()

        for i in nums:
            duplicate.add(i)

        if len(duplicate) == len(nums):
            return False
        else:
            return True
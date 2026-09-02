class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        resLen, count = 0, 0

        for n in nums:
            if n == 0:
                resLen = max(resLen, count)
                count = 0
            else:
                count += 1

        return max(resLen, count)
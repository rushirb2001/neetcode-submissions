class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        n = len(nums)
        l, total = 0, 0
        for r in range(n):
        #     curSum = 0
        #     for j in range(i, n):
        #         curSum += nums[j]
        #         if curSum >= target:
        #             res = min(res, j - i + 1)
        #             break

        # return 0 if res == float("inf") else res
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res


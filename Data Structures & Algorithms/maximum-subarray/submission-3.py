class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # res = nums[0]

        # for i in range(len(nums)):
        #     cur = 0
        #     for j in range(i, len(nums)):
        #         cur += nums[j]
        #         res = max(res, cur)

        # return res

        memo = {}

        def dfs(i, flag):
            if i == len(nums) - 1:
                return max(0, nums[i]) if flag else nums[i]
            if (i, flag) in memo:
                return memo[(i, flag)]

            if flag:
                memo[(i, flag)] = max(0, nums[i] + dfs(i+1, True))
            else:
                memo[(i, flag)] = max(dfs(i+1, False), nums[i] + dfs(i+1, True))

            return memo[(i, flag)]
        
        return dfs(0, False)
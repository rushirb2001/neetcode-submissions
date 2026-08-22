class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # memo = {}

        # def dfs(i):
        #     if i == len(nums) - 1:
        #         return 0
        #     if nums[i] == 0:
        #         return float('inf')
            
        #     if i in memo:
        #         return memo[i]
            
        #     res = float("inf")
        #     end = min(len(nums) - 1, i + nums[i])
        #     for j in range(i + 1, end + 1):
        #         res = min(res, 1 + dfs(j))
            
        #     memo[i] = res
            
        #     return res

        # return dfs(0)
        n = len(nums)
        dp = [float("inf")] * n

        dp[n - 1] = 0

        for i in range(n - 2, -1, -1):
            end = min(n - 1, nums[i] + i)
            for j in range(i + 1, end + 1):
                dp[i] = min(dp[i], 1 + dp[j])

        return dp[0]
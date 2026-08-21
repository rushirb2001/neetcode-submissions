class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # memo = [[-1] * (n + 1) for _ in range(n)]
        # def dfs(i, j):
        #     if i == len(nums):
        #         return 0
        #     if memo[i][j+1] != -1:
        #         return memo[i][j+1]
            
        #     LIS = dfs(i + 1, j)
            
        #     if j == -1 or nums[j] < nums[i]:
        #         LIS = max(LIS, 1 + dfs(i + 1, i))
            
        #     memo[i][j + 1] = LIS

        #     return LIS


        # return dfs(0, -1)

        n = len(nums)
        memo = [-1] * n

        def dfs(i):
            if memo[i] != -1:
                return memo[i]

            LIS = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))

            memo[i] = LIS
            return LIS

        return max(dfs(i) for i in range(n))
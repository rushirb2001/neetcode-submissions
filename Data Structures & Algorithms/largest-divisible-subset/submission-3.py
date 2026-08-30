class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo = {}
        def dfs(i):
            if i == len(nums): return []
            if i in memo: return memo[i]
            longest = [nums[i]]
            for j in range(i+1,len(nums)):
                if nums[j]%nums[i]: continue
                path = [nums[i]]+dfs(j)
                if len(path) > len(longest):
                    longest = path
            memo[i] = longest
            return longest
        return dfs(0)
            
        # cache = {}

        # def dfs(i):
        #     if i in cache:
        #         return cache[i]

        #     res = [nums[i]]

        #     for j in range(i+1, len(nums)):
        #         if nums[j] % nums[i] == 0:
        #             tmp = [nums[i]] + dfs(j)
        #             if len(tmp) > len(res):
        #                 res = tmp

        #     cache[i] = res
        #     return res

        # res = []
        # for i in range(len(nums)):
        #     tmp = dfs(i)
        #     if len(tmp) > len(res):
        #         res = tmp

        # return res
        # dp = [[num] for num in nums]
        # res = []

        # for i in range(len(nums) - 1, -1, -1):
        #     for j in range(i+1, len(nums)):
        #         if nums[j] % nums[i] == 0:
        #             tmp = [nums[i]] + dp[j]
        #             dp[i] = tmp if len(tmp) > len(dp[i]) else dp[i]
            
        #     res = dp[i] if len(dp[i]) > len(res) else res

        # return res

# 1 4 2 9 3 8 -> 1 2 3 4 8 9 -> 1 > 2 - 3 - 4 - 8 - 9

# 1 2 3 4 8 9 = dp

# num = 9, i = 5 -> 9 -> res = 3
# num = 8, i = 4 -> 8 and 9 -> inner loop is satisfied, tmp = 8 and 9 -> dp = tmp as [8, 9] > [9] -> res = dp as at. i = 4, dp = [8, 9] > [9] 
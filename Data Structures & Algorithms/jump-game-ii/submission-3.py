class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memo = {}

        def dfs(i):
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return float('inf')
            
            if i in memo:
                return memo[i]
            
            res = float("inf")
            end = min(len(nums) - 1, i + nums[i])
            for j in range(i + 1, end + 1):
                res = min(res, 1 + dfs(j))
            
            memo[i] = res
            
            return res

        return dfs(0)
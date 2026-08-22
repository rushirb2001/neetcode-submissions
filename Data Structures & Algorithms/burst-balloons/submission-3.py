class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # How to obtain the maximum? let's recurse
        # At every instance, you can choose to burst a balloon from index 0 to n-1
        # given a list balloons, pop one and receive the reward (then backtrack to put it back)
        # return the total amount that you get;
        # base case, there's only 1 balloon left.
        dp = {}

        def dfs(balloons):
            if len(balloons) == 1:
                return balloons[0]
            tuple_lst = tuple(balloons)
            if tuple_lst in dp:
                return dp[tuple_lst]
            score = 0
            for i in range(len(balloons)):
                # choose to pop or not
                left = 1
                if i-1 >= 0:
                    left = balloons[i-1]
                right = 1
                if i + 1 < len(balloons):
                    right = balloons[i+1]
                gained_score = balloons[i] * left * right
                val = balloons.pop(i)
                score = max(score, dfs(balloons) + gained_score)

                balloons.insert(i, val)
            dp[tuple_lst] = score
            return score
        
        return dfs(nums)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}

        def dfs(r, c, prevVal):
            if (r < 0 or c < 0) or r >= ROWS or c >= COLS or matrix[r][c] <= prevVal:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]

            res = 0
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            memo[(r,c)] = res
            return res

        LIP = 0
        for r in range(ROWS):
            for c in range(COLS):
                LIP = max(LIP, dfs(r, c, float("-inf")))

        return LIP







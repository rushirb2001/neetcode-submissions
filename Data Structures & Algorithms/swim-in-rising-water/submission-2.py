class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # n = len(grid)
        # visit = [[False] * n for _ in range(n)]

        # def dfs(r, c, t):
        #     if min(r, c) < 0 or max(r, c) >= n or visit[r][c]:
        #         return 1000000
        #     if r == (n - 1) and c == (n - 1):
        #         return max(t, grid[r][c])
        #     visit[r][c] = True
        #     t = max(t, grid[r][c])
        #     res = min(dfs(r + 1, c, t),
        #                dfs(r - 1, c, t),
        #                dfs(r, c + 1, t),
        #                dfs(r, c - 1, t))
        #     visit[r][c] = False
        #     return res

        # return dfs(0, 0, 0)

        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]  # (time/max-height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or
                    neiR == N or neiC == N or
                    (neiR, neiC) in visit
                ):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
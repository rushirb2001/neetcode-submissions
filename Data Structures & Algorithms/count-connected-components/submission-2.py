class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        visit = [False] * n
        res = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # def dfs(node):
        #     for nei in adj[node]:
        #         if not visit[nei]:
        #             visit[nei] = True
        #             dfs(nei)
        
        # for node in range(n):
        #     if not visit[node]:
        #         visit[node] = True
        #         dfs(node)
        #         res += 1

        # return res

        def bfs(node):
            q = deque([node])
            visit[node] = True
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if not visit[nei]:
                        visit[nei] = True
                        q.append(nei)

        for node in range(n):
            if not visit[node]:
                bfs(node)
                res += 1

        return res
class Solution:



    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = [[] for _ in range(numCourses)]
        ispreReq = [[-1] * numCourses for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[v].append(u)
            ispreReq[v][u] = True

        def dfs(node, target):
            if ispreReq[node][target] != -1:
                return ispreReq[node][target] == 1
            
            for nei in adj[node]:
                if nei == target or dfs(nei, target):
                    ispreReq[node][target] = 1
                    return True
            
            ispreReq[node][target] = 0
            return False

        res = []
        for u, v in queries:
            res.append(dfs(v, u))

        return res
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            if adj[crs] == []:
                return True
            
            visited.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            adj[crs] = []

            return True



        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True


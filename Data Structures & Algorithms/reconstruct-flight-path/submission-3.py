class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)

        for key in adj:
            adj[key].sort()

        res = []

        def dfs(src):
            while adj[src]:
                dest = adj[src].pop(0)  # takes lexicographically smallest
                dfs(dest)
            res.append(src)

        dfs("JFK")
        print(res)
        return res[::-1]
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):

            # Breakout Conditions: Backtracking (Goal and Direction Condition)
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target or i == len(candidates):
                return

            # Backtracking Candidate generation
            cur.append(candidates[i])

            # Branching Conditions: 1. Go with same number additions and proceed
            dfs(i+1, cur, total + candidates[i])

            # Branching Conditions: 2. Go with different additions while skipping duplicates. 
            cur.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res

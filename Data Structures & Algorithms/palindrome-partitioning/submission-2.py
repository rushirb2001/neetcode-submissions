class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, cur = [], []

        def dfs(start, end):
            if end >= len(s):
                if start == len(s):  # All characters used
                    res.append(cur.copy())
                return
            
            # Option 1: Extend current substring
            dfs(start, end + 1)
            
            # Option 2: If s[start:end+1] is palindrome, use it and move on
            k = s[start:end + 1]
            if k == k[::-1]:
                cur.append(k)
                dfs(end + 1, end + 1)  # Start new substring after current
                cur.pop()

        dfs(0, 0)
        return res
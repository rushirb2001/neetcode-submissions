class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # res = set()

        # def dfs(i, cur):
        #     if len(cur) == 3:
        #         if cur[0] == cur[2]:
        #             res.add(cur)
        #         return
        #     if i == len(s):
        #         return
            
        #     dfs(i+1, cur)
        #     dfs(i+1, cur + s[i])

        # dfs(0, "")
        # return len(res)

        # res = set()
        # n = len(s)

        # for i in range(n - 3):
        #     for j in range(i + 1, n - 2):
        #         for k in range(j + 1, n - 1):
        #             if s[i] != s[k]:
        #                 continue
        #             res.add(s[i] + s[j] + s[k])

        res = 0
        for ends in range(ord('a'), ord('z') + 1):
            for mid in range(ord('a'), ord('z') + 1):
                seq = chr(ends) + chr(mid) + chr(ends)
                idx, found = 0, 0
                for c in s:
                    if seq[idx] == c:
                        idx += 1
                        if idx == 3:
                            found = 1
                            break
                res += found
        
        return res
        # return len(res)

        


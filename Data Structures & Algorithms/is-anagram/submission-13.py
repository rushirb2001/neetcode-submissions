class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            a, b = defaultdict(int), defaultdict(int)
            for i in range(len(s)):
                a[s[i]] += 1
                b[t[i]] += 1
            print(a,b)
            return a == b
        return False
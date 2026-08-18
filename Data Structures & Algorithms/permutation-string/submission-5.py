class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = sorted(s1)
        k = len(s)

        for i in range(len(s2)-k+1):
            ss = sorted(s2[i:i+k])
            if s == ss:
                return True
        return False
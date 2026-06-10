class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = sorted(s1)
        k = len(s)

        for i in range(len(s2) - k + 1):
            ss = []
            for j in range(0, k):
                ss.append(s2[i+j])
            print(s, sorted(ss))
            if s == sorted(ss):
                return True
        
        return False
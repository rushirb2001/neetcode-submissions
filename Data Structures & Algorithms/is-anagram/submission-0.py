class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ssstr = sorted(s)
        tsstr = sorted(t)

        if ssstr == tsstr:
            return True
        
        return False
class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        asc = [ord(c) for c in s]

        for i in range(len(s)-1):
            score += abs(asc[i] - asc[i+1])
        
        return score
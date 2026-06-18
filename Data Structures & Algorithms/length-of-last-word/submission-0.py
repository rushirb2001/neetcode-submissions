class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        length = 0
        for w in words:
            if w:
                length = len(w)
        return length
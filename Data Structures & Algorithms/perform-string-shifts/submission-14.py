class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = 0
        for d, a in shift:
            total_shift += a if d == 0 else -a
        
        n = len(s)
        total_shift %= n

        return s[total_shift:] + s[:total_shift]
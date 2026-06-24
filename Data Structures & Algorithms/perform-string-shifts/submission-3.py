class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        slide = 0
        for side in shift:
            if side[0]:
                slide -= side[1]
            else:
                slide += side[1]
        
        slide %= len(s)
        return s[slide:] + s[:slide]
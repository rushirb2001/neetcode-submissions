class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        lastIndex = 0
        alphaIndex = {}

        for i, k in enumerate(keyboard):
            alphaIndex[k] = i

        totalMoves = 0

        for c in word:
            totalMoves += abs(alphaIndex[c] - lastIndex)
            lastIndex = alphaIndex[c]

        return totalMoves        
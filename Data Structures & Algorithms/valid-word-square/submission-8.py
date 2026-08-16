class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rows = len(words)
        cols = 0
        for w in words:
            cols = max(cols, len(w))
        
        if rows == cols:
            for i in range(len(words)):
                l = len(words[i])
                if l < cols:
                    words[i] = words[i] + " "*(cols-l)

            for i in range(rows):
                for j in range(i+1, cols):
                    print(i,j,words[i][j],words[j][i])
                    if words[i][j] != words[j][i]:
                        print(i,j,words[i][j],words[j][i])
                        return False
        
            return True
        
        return False

# b a l l
# a s e e
# l e t _
# l e p _
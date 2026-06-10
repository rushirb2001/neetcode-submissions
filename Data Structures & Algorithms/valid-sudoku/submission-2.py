class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hmap = [[],[],[]]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                row, col, sq = f"Digit {board[i][j]} in Row {i+1}",f"Digit {board[i][j]} in Column {j+1}",f"Digit {board[i][j]} in Square {(i // 3, j // 3)}"
                if row in hmap[0] or col in hmap[1] or sq in hmap[2]:
                    return False
                else:
                    hmap[0].append(row)
                    hmap[1].append(col)
                    hmap[2].append(sq)

        return True
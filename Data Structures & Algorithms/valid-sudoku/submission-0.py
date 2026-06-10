class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        prefix = ['in row','in col','in box']
        bd = set()
        for i in range(9):
            for j in range(9):
                val = str(board[i][j])
                if val != '.':
                    astr, bstr, cstr = str(val+prefix[0]+str(i)), str(val+prefix[1]+str(j)), str(val+prefix[2]+str(i//3)+'-'+str(j//3))
                    if astr in bd or bstr in bd or cstr in bd:
                        return False
                    else:
                        bd.add(astr)
                        bd.add(bstr)
                        bd.add(cstr)
        
        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        prefix = ['in row','in col','in box']
        """
        Prefixes to create strings
        """

        bd = set()
        """
        String based set collection to satisfy the three-conditions
        """

        for i in range(9):
            for j in range(9):
                """
                Double Array iteration to set rows, columns and the square 3x3 matrix in the sudoku board
                """
                val = str(board[i][j])
                if val != '.':
                    astr, bstr, cstr = str(val+prefix[0]+str(i)), str(val+prefix[1]+str(j)), str(val+prefix[2]+str(i//3)+'-'+str(j//3))
                    """
                    Creating row, column and square string to be added to set collection
                    """

                    if astr in bd or bstr in bd or cstr in bd:
                        """
                        If a duplicate of the string already existed in the set collection than we directly just exit
                        """
                        return False
                    else:
                        bd.add(astr)
                        bd.add(bstr)
                        bd.add(cstr)
        
        return True


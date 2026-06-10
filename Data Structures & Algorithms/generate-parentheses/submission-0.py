class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(leftN, rightN):
            if leftN == rightN == n:
                res.append("".join(stack))
                return

            if leftN < n: # Initiating Condition and Condition to not put wrong order of parenthesis
                stack.append("(") # Base Condition to put the starting parenthesis
                backtrack(leftN + 1, rightN)  # Tree Recursive call
                stack.pop() # Pops the last element to push into other variations also
            
            if rightN < leftN: # Closing condition to put end the continuing parenthesis
                stack.append(")") # Close Condition to end the last parenthesis 
                backtrack(leftN, rightN + 1) # Tree Recursive call
                stack.pop() # Pops the last element to allow for closed parenthesis beyond previous conditions
        
        backtrack(0,0) # Starts the tree at '(' continuing until the last string end.
        return res
        
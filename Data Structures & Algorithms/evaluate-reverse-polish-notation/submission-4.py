class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in "+-*/":
                # Operator - pop operands and apply operation
                if t == "+":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b + a)
                elif t == "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif t == "*":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b * a)
                elif t == "/":
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))  # truncate toward zero
            else:
                # Operand - convert to int and push
                stack.append(int(t))
        
        return stack[0]
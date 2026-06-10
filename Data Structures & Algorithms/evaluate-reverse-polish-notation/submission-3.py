class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for t in tokens:
            if t == '+':
                res = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif t == '-':
                res = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif t == '*':
                res = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif t == '/':
                res = stack[-2] / stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(res))
            else:
                stack.append(int(t))
                print(stack)
            
        return int(stack[-1])
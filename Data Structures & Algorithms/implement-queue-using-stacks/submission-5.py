class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        # while len(self.stack1) > 1:
        #     self.stack2.append(self.stack1.pop())
        # res = self.stack1.pop()
        # while self.stack2:
        #     self.stack1.append(self.stack2.pop())
        # return res
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        # while len(self.stack1) > 1:
        #     self.stack2.append(self.stack1.pop())
        # res = self.stack1[-1]
        # while self.stack2:
        #     self.stack1.append(self.stack2.pop())
        # return res
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
        
    def empty(self) -> bool:
        # return not self.stack1
        return max(len(self.stack1), len(self.stack2)) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
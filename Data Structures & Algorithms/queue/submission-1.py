class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head, self.tail = Node(-1), Node(-1)
        self.head.next, self.tail.prev = self.tail, self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        node = Node(value)
        last = self.tail.prev

        last.next, node.prev = node, last
        node.next, self.tail.prev = self.tail, node

    def appendleft(self, value: int) -> None:
        node = Node(value)
        first = self.head.next

        self.head.next, node.next = node, first
        node.prev, first.prev = self.head, node

    def pop(self) -> int:
        if not self.isEmpty():
            last = self.tail.prev
            sec = last.prev

            sec.next, self.tail.prev = self.tail, sec

            return last.val

        return -1
        

    def popleft(self) -> int:
        if not self.isEmpty():
            first = self.head.next
            sec = first.next

            sec.prev, self.head.next = self.head, sec

            return first.val

        return -1
        

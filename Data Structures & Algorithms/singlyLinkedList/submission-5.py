class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        cur = self.head.next

        while cur:
            if i == index:
                return cur.val
            
            i += 1
            cur = cur.next

        return -1
        

    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node

        if not node.next:
            self.tail = node
        

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        i = 0
        cur = self.head

        while i < index and cur:
            i += 1
            cur = cur.next

        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True

        return False
        

    def getValues(self) -> List[int]:

        arr = []
        cur = self.head.next

        while cur:
            arr.append(cur.val)
            cur = cur.next

        return arr
        

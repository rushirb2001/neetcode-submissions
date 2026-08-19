"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        deepCopy = collections.defaultdict(lambda: Node(0))
        deepCopy[None] = None

        cur = head
        while cur:
            deepCopy[cur].val = cur.val
            deepCopy[cur].next = deepCopy[cur.next]
            deepCopy[cur].random = deepCopy[cur.random]
            cur = cur.next

        return deepCopy[head]
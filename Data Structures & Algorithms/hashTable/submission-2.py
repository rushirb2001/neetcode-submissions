class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0 # Gets maintained as we move forward while adding and removing
        self.table = [None] * self.capacity # Class node based storage.

    def hasher(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hasher(key)
        node = self.table[index]

        if not node:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            prev = None
            while node:
                if node.key == key:
                    node.val = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)
            self.size += 1
        
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hasher(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.val
            node = node.next
        
        return -1

    def remove(self, key: int) -> bool:
        index = self.hasher(key)
        node = self.table[index]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                self.size -= 1
                return True

            prev, node = node, node.next

        return False


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for node in self.table:
            while node:
                index = node.key % new_capacity
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.val)
                else:
                    new_node = new_table[index]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.val)
                node = node.next

        self.capacity = new_capacity
        self.table = new_table


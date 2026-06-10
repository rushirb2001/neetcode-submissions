class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if not self.root:
            self.root = new_node
            return
        
        cur = self.root
        while True:
            if key < cur.key:
                if not cur.left:
                    cur.left = new_node
                    return
                cur = cur.left
            elif key > cur.key:
                if not cur.right:
                    cur.right = new_node
                    return
                cur = cur.right
            else:
                cur.val = val
                return

    def get(self, key: int) -> int:
        cur = self.root
        while cur:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return cur.val
        return -1



    def getMin(self) -> int:

        if not self.root:
            return -1

        cur = self.root
        while cur and cur.left:
            cur = cur.left

        return cur.val if cur else -1



    def getMax(self) -> int:

        if not self.root:
            return -1

        cur = self.root
        while cur and cur.right:
            cur = cur.right

        return cur.val if cur else -1


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, cur: TreeNode, key: int) -> TreeNode:
        if cur == None:
            return None

        if key > cur.key:
            cur.right = self.removeHelper(cur.right, key)
        elif key < cur.key:
            cur.left = self.removeHelper(cur.left, key)
        else:
            if cur.left == None:
                return cur.right
            elif cur.right == None:
                return cur.left
            else:
                minNode = self.findMin(cur.right)
                cur.key = minNode.key
                cur.val = minNode.val
                cur.right = self.removeHelper(cur.right, minNode.key)
        
        return cur

    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node


    def getInorderKeys(self) -> List[int]:
        arr = []
        self.InOrderTraverser(self.root, arr)
        return arr

    def InOrderTraverser(self, root: TreeNode, arr: List[int]) -> None:
        if root:
            self.InOrderTraverser(root.left, arr)
            arr.append(root.key)
            self.InOrderTraverser(root.right, arr)




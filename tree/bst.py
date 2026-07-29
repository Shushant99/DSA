
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

 
class BST:
    def __init__(self):
        self.root = None
 
    # ---------- Insert ----------
    def insert(self, value):
        self.root = self._insert(self.root, value)
 
    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        # duplicate keys are ignored
        return node
 
    # ---------- Search ----------
    def search(self, value):
        return self._search(self.root, value)
 
    def _search(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)
 
    # ---------- Delete ----------
    def delete(self, value):
        self.root = self._delete(self.root, value)
 
    def _delete(self, node, value):
        if node is None:
            return None
 
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Node found: handle 3 cases
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
 
            # Two children: replace with inorder successor (min of right subtree)
            successor = self._find_min(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)
 
        return node
 
    # ---------- Min / Max ----------
    def find_min(self):
        if self.root is None:
            return None
        return self._find_min(self.root).value
 
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
 
    def find_max(self):
        if self.root is None:
            return None
        return self._find_max(self.root).value
 
    def _find_max(self, node):
        while node.right is not None:
            node = node.right
        return node
 
    # ---------- Height ----------
    def height(self):
        return self._height(self.root)
 
    def _height(self, node):
        if node is None:
            return -1  # empty tree has height -1; single node has height 0
        return 1 + max(self._height(node.left), self._height(node.right))
 
    # ---------- Size ----------
    def size(self):
        return self._size(self.root)
 
    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)
 
    # ---------- Traversals ----------
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
 
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)
 
    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result
 
    def _preorder(self, node, result):
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
 
    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result
 
    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)
 
    def is_empty(self):
        return self.root is None
    
s= BST()
s.insert(5)
s.insert(6)
s.insert(2)
print(s.postorder())
print(s.size())
print(s.height())
print(s.find_max())

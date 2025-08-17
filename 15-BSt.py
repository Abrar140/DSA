class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_rec(self.root, data)

    def _insert_rec(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert_rec(node.left, data)
        elif data > node.data:
            node.right = self._insert_rec(node.right, data)
        # if data == node.data, do nothing or handle duplicates here
        return node

    def search(self, data):
        return self._search_rec(self.root, data)

    def _search_rec(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_rec(node.left, data)
        else:
            return self._search_rec(node.right, data)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

# Example usage:
bst = BST()
values = [10, 5, 15, 2, 7, 12, 20]
for val in values:
    bst.insert(val)

print("Inorder traversal:")
bst.inorder(bst.root)
print("\nSearch 7:", bst.search(7))
print("Search 25:", bst.search(25))

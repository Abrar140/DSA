class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return

        # Insert using level order traversal to find the first empty spot
        queue = [self.root]
        while queue:
            node = queue.pop(0)

            if not node.left:
                node.left = new_node
                return
            else:
                queue.append(node.left)

            if not node.right:
                node.right = new_node
                return
            else:
                queue.append(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

# Example Usage
bt = BinaryTree()
for val in [10, 20, 30, 40, 50, 60]:
    bt.insert(val)

print("Preorder traversal:")
bt.preorder(bt.root)
print("\nInorder traversal:")
bt.inorder(bt.root)
print("\nPostorder traversal:")
bt.postorder(bt.root)

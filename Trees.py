'''Implementing Node class, BinaryTree class, traversing InOrder, PreOrder and PostOrder'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, value):
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def inorder_traversal(self, node):
        if node is None: return
        self.inorder_traversal(node.left)
        print(node.value)
        self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node is None: return
        print(node.value)
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node is None: return
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.value)

# Example usage
tree = BinaryTree(4)
tree.insert(2)
tree.insert(6)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(7)

print("Inorder traversal:")
tree.inorder_traversal(tree.root)
print("preorder traversal:")
tree.preorder_traversal(tree.root)
print("postorder traversal:")
tree.postorder_traversal(tree.root)     

class Node:
    """
    A class to represent a node in a binary tree.
    """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    """
    A class to represent a binary search tree (BST).
    """
    def create_node(self, data):
        """
        Creates and returns a new node with the given data.
        """
        return Node(data)
    
    def insert(self, node, data):
        """
        Inserts a new node with the given data into the BST.
        """
        try:
            if node is None:
                return self.create_node(data)
            if data < node.data:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)
            return node
        except Exception as e:
            print("Error inserting node:", e)
    
    def traverse_inorder(self, root):
        """
        Performs an inorder traversal of the BST.
        """
        try:
            if root is not None:
                self.traverse_inorder(root.left)
                print(root.data, end=" ")
                self.traverse_inorder(root.right)
        except Exception as e:
            print("Error during inorder traversal:", e)

if __name__ == "__main__":
    tree = Tree()
    root = tree.create_node(5)
    print("Root node:", root.data)
    tree.insert(root, 2)
    tree.insert(root, 10)
    tree.insert(root, 7)
    tree.insert(root, 15)
    tree.insert(root, 12)
    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 6)
    tree.insert(root, 8)
    
    print("\nInorder Traversal:")
    tree.traverse_inorder(root)
    print()

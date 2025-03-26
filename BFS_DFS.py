class Node:
    """
    A class to represent a node in a binary tree.
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs(root):
    """
    Performs a breadth-first search (BFS) traversal on the tree.
    """
    try:
        if root is None:
            return []
        queue = []
        visited = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            visited.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return visited
    except Exception as e:
        print("Error during BFS traversal:", e)


def dfspreorder(root):
    """
    Performs a depth-first search (DFS) preorder traversal on the tree.
    """
    try:
        visited = []

        def traverse(node):
            if node:
                visited.append(node.val)
                traverse(node.left)
                traverse(node.right)
        
        traverse(root)
        return visited
    except Exception as e:
        print("Error during preorder traversal:", e)


def dfsinorder(root):
    """
    Performs a depth-first search (DFS) inorder traversal on the tree.
    """
    try:
        visited = []

        def traverse(node):
            if node:
                traverse(node.left)
                visited.append(node.val)
                traverse(node.right)
        
        traverse(root)
        return visited
    except Exception as e:
        print("Error during inorder traversal:", e)


def dfspostorder(root):
    """
    Performs a depth-first search (DFS) postorder traversal on the tree.
    """
    try:
        visited = []

        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                visited.append(node.val)
        
        traverse(root)
        return visited
    except Exception as e:
        print("Error during postorder traversal:", e)


if __name__ == "__main__":
    n = Node(1)
    n.left = Node(2)
    n.right = Node(3)
    n.left.left = Node(4)
    
    print("Root, Left, Right, Left-Left:", n.val, n.left.val, n.right.val, n.left.left.val)
    print("BFS Traversal:", bfs(n))
    print("Preorder Traversal:", dfspreorder(n))
    print("Inorder Traversal:", dfsinorder(n))
    print("Postorder Traversal:", dfspostorder(n))
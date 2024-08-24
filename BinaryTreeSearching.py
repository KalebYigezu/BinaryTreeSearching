class Node:
    def __init__(self, k):
        self.data = k
        self.left = None
        self.right = None

def searchDFS(root, value):
    if root is None:
        return False
    if root.data == value:
        return True
    left_res = searchDFS(root.left, value)
    right_res = searchDFS(root.right, value)

    return left_res or right_res


if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)

    value = 6
    if searchDFS(root, value):
        print(f"{value} is found in the binary tree")
    else:
        print(f"{value} is not found in the binary tree")

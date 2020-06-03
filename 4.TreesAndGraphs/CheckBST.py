class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBST(root, min, max):
    if root is None:
        return True
    
    if root.data <= min or root.data > max:
        return False

    return checkBST(root.left, min, root.data) and checkBST(root.right, root.data, max)

if __name__ == "__main__":
    node25 = Node(25)
    node5 = Node(5)


    node10 = Node(10)
    node10.left = node5

    node15 = Node(15)

    node10.right = node15

    node15.right = node25

    print(checkBST(node10, -100000, 100000))
    
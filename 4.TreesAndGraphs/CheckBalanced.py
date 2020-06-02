class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBalanced(node):
    if node is None:
        return 0
    
    leftHeight = checkBalanced(node.left)
    if leftHeight == -1:
        return -1

    rightHeight = checkBalanced(node.right)
    if rightHeight == -1:
        return -1
    
    if abs(leftHeight - rightHeight) > 1:
        return -1
    
    return 1+max(leftHeight, rightHeight)

if __name__ == "__main__":
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node2 = Node(2)
    node2.left = node4
    node2.right = node5

    node3 = Node(3)
    node3.left = node6
    
    node6.right = node7

    node1 = Node(1)
    node1.left = node2
    node1.right = node3

    print(checkBalanced(node1))
class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent 


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def findMinInRight(node):
    node = node.right
    while node.left!=None:
        node = node.left
    return node

def findRightParent(node):
    parent = node.parent
    if parent == None:
        return None
    if parent.left!=None and parent.left.data == node.data:
        return parent
    else:
        return findRightParent(node.parent)

def findSuccessor(node):
    if node.right!=None:
        return findMinInRight(node)    
    else:
        return findRightParent(node)
        
            
        

if __name__ == "__main__":
    node15 = Node(15, None)
    
    node6 = Node(6, node15)
    node15.left = node6
    node3 = Node(3, node6)
    node2 = Node(2, node3)
    node4 = Node(4, node3)
    node3.left = node2
    node3.right = node4
    node6.left = node3

    node7 = Node(7, node6)
    node6.right = node7
    node13 = Node(13, node7)
    node7.right = node13
    node9 = Node(9, node13)
    node13.left = node9

    node18 = Node(18, node15)
    node15.right = node18

    node17 = Node(17, node18)
    node18.left = node17

    node26 = Node(26, node18)
    node18.right = node26

    print(findSuccessor(node26).data)




    
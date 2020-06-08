from binarytree import bst, Node
import copy


def isSubTree(bigTree, smallTree):
    if bigTree == None:
        return False
    elif bigTree.value == smallTree.value and matchTree(bigTree, smallTree):
        return True
    else:
        return isSubTree(bigTree.left, smallTree) or isSubTree(bigTree.right, smallTree)

def matchTree(tree1, tree2):
    if tree1 == None and tree2 == None:
        return True
    elif tree1 == None or tree2 == None:
        return False
    elif tree1.value != tree2.value:
        return False
    else:
        return matchTree(tree1.left, tree2.left) and matchTree(tree1.right, tree2.right)
    
if __name__ == "__main__":
    node4 = Node(4)
    node1 = Node(1)
    node10 = Node(10)

    node4.left = node1
    node4.right = node10

    node16 = Node(16)
    node32 = Node(32)
    node1.left = node16
    node1.right = node32

    node41 = Node(41)
    node76 = Node(76)

    node10.left = node41
    node10.right = node76

    bigTree = node4

    smallTree = node10

    #print(isSubTree(bigTree , smallTree))

    smallTreeUnIdentical = copy.copy(node10)
    smallTreeUnIdentical.left = Node(222)

    print(isSubTree(bigTree, smallTreeUnIdentical))



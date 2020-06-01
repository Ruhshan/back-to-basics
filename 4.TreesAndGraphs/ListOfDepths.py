class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getListOfDepth(node,depth,lst):
    if not node: 
        return None
    if lst.get(depth) == None:
        lst[depth] = [node.data]
    else:
        lst[depth].append(node.data)

    getListOfDepth(node.left,depth+1,lst) 
    getListOfDepth(node.right,depth+1,lst)

    return lst

    

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
    node3.right = node7

    node1 = Node(1)
    node1.left = node2
    node1.right = node3

    lst = getListOfDepth(node1,1,{})

    print(lst)


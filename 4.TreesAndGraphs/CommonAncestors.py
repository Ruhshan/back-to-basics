class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(node): 
    if not node: 
        return
      
    print(node.data) 
    preOrder(node.left) 
    preOrder(node.right)  


def pathTo(root, node):
	if root == None:
		return None
	
	if root.data == node.data:
		path = [root.data]
		return path

	leftPath = pathTo(root.left, node)
	rightPath = pathTo(root.right, node)

	if leftPath != None:
		leftPath.append(root.data)
		return leftPath
	
	if rightPath != None:
		rightPath.append(root.data)
		return rightPath
	
	return None

def commonAncestor(root, node1,node2):
	node1Path = pathTo(root, node1)
	node2Path = pathTo(root, node2)

	prev = None
	while len(node1Path) != 0 and len(node2Path) != 0:
		n1 = node1Path.pop()
		n2 = node2Path.pop()

		if n1 != n2:
			break
		prev = n1
	
	return prev 


if __name__ == "__main__":
	node2 = Node(2)
	node4 = Node(4)
	node1 = Node(1)

	node2.left = node4
	node2.right = node1 

	node10 = Node(10)
	node12 = Node(12)
	node4.left = node10
	node4.right = node12

	node13 = Node(13)
	node5 = Node(5)
	node1.left = node13
	node1.right = node5

	node17 = Node(17)

	node5.right = node17

	print(commonAncestor(node2, node17, node13))


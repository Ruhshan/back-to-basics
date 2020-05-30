class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sortedArrayToBST(arr):
    
    if len(arr)==0:
        return None
    
    midIndex = len(arr)/2
    midVal = arr[midIndex]
    
    midNode = Node(midVal)
    midNode.left = sortedArrayToBST(arr[:midIndex])
    midNode.right = sortedArrayToBST(arr[midIndex+1:])

    return midNode

def preOrder(node): 
    if not node: 
        return
      
    print(node.data) 
    preOrder(node.left) 
    preOrder(node.right)  

    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]

    root = sortedArrayToBST(arr)

    preOrder(root)

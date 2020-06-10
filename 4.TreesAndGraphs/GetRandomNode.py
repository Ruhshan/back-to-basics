import random
class Node:
    def __init__(self, data):
        self.data = data
        self.size = 1
        self.left = None
        self.right = None

    def getRandomNode(self):
        leftSize = 0
        if self.left !=None:
            leftSize = self.left.size
        randIndex = random.randint(0, self.size-1)

        if randIndex<leftSize:
            return self.left.getRandomNode()
        elif randIndex == leftSize:
            return self.data 
        else:
            return self.right.getRandomNode()


    def insert(self, data):
        if data <= self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        self.size+=1


def preOrder(node): 
    if not node: 
        return
      
    print(node.data) 
    preOrder(node.left) 
    preOrder(node.right)  


if __name__ == "__main__":
    node4 = Node(4)
    # node1 = Node(1)
    # node10 = Node(10)

    # node4.left = node1
    # node4.right = node10

    # node16 = Node(16)
    # node32 = Node(32)
    # node1.left = node16
    # node1.right = node32

    # node41 = Node(41)
    # node76 = Node(76)

    # node10.left = node41
    # node10.right = node76

    # print(node1.size)

    node4.insert(1)
    node4.insert(10)
    node4.insert(5)

    print(node4.getRandomNode())
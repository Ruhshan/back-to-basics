class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)

            if self.head.next == None:
                self.head.next = newNode
                self.tail = newNode
            else:
                self.tail.next = newNode
                self.tail = newNode
    
    def printlist(self):
        temp = self.head
        while temp!=None:
            print(temp.data, temp)
            temp=temp.next
    
    def appendNode(self, node):
        if self.head == None:
            self.head = node
        else:
            if self.head.next == None:
                self.head.next = node
                self.tail = node 
            else:
                self.tail.next = node
                self.tail = node

def findIntersection(ll1, ll2):
    ll1size, ll1tail = getSizeAndTaile(ll1)
    ll2size, ll2tail = getSizeAndTaile(ll2)

    if ll1tail != ll2tail:
        return None
    
    if ll1size> ll2size:
        longerListNode = ll1.head
        shorterListNode = ll2.head
    else:
        longerListNode = ll2.head
        shorterListNode = ll1.head

    diff = abs(ll1size - ll2size)

    longerListNode = getNthNode(longerListNode, diff)

    while longerListNode!=None:
        if longerListNode == shorterListNode:
            return longerListNode
        longerListNode = longerListNode.next
        shorterListNode = shorterListNode.next


def getNthNode(node, n):
    count = 0

    while node!=None:
        count+=1
        node = node.next

        if count == n:
            return node

def getSizeAndTaile(ll):
    node = ll.head
    size = 1
    while node.next!=None:
        size+=1
        node = node.next
    return size, node


if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()

    intersection = Node(4)

    ll1.appendNode(Node(0))
    ll1.appendNode(Node(2))
    ll1.appendNode(intersection)
    ll1.appendNode(Node(6))
    ll1.appendNode(Node(8))


    ll2.appendNode(Node(1))
    ll2.appendNode(Node(3))
    ll2.appendNode(Node(10))
    ll2.appendNode(Node(11))
    ll2.appendNode(intersection)
    
    intersection = findIntersection(ll1, ll2)

    print(intersection.data)








class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previus = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = Node(data)
        else:
            if self.tail == None:
                self.head.next = newNode
                newNode.previus = self.head
                self.tail = newNode
            else:
                newNode.previus = self.tail
                self.tail.next = newNode
                self.tail = newNode
                
    def printList(self):
        temp = self.head 
        while temp!=None:
            print(temp.data)
            temp = temp.next

    def printReverse(self):
        temp = self.tail
        while temp!=None:
            print(temp.data)
            temp = temp.previus

            

if __name__=='__main__':
    dll = DoublyLinkedList()

    dll.append(0)
    dll.append(1)
    dll.append(2)

    dll.printReverse()

    dll.printList()


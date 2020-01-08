import gc
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
    
    def push(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.previus = newNode
            self.head = newNode

    def _delete(self, node, data):
        
        if node.data == data:
            if node.previus == None:
                self.head = self.head.next
                self.head.previus = None
            elif node.next == None:
                self.tail = self.tail.previus
                self.tail.next = None 
            else:
                node.previus.next = node.next
                node.next.previus= node.previus
                return

        else:
            return self._delete(node.next, data)
            
    def delete(self,data):
        return self._delete(self.head, data)

                
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

            



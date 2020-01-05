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

    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode= Node(data)
            newNode.next = self.head
            self.head = newNode

    def insertAfter(self, nodeVal, data):
        temp = self.head
        while temp!=None:
            if temp.data == nodeVal:
                newNode = Node(data)
                newNode.next = temp.next
                temp.next = newNode
                break  
            temp=temp.next

    def deleteNode(self, nodeVal):
        temp = self.head
        while temp!=None:
            if temp.data == nodeVal:
                prev.next  = temp.next    
                break
            prev = temp
            temp = temp.next

    def _getLength(self, node):
        if not node:
            return 0
        else:
            return 1 + self._getLength(node.next)
    
    def getLn(self):
        return self._getLength(self.head)
    
    def _search(self, node, key):
        if not node:
            return False
        elif node.data == key:
            return True
        else:
            return self._search(node.next, key)

    def search(self, key):
        return self._search(self.head, key)


    def printlist(self):
        temp = self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next



if __name__=='__main__':
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.push(0)
    llist.insertAfter(2,7)

    llist.printlist()  

    #llist.deleteNode(3)
    
    print(llist.getLn())
    #llist.printlist()
    # 
    print(llist.search(12))       

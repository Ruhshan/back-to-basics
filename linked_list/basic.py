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
    

    llist.printlist()        
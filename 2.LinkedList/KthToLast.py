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
            print(temp.data)
            temp=temp.next
    
    def getKthTolast(self, k):
        p1 = self.head
        p2 = self.head

        for i in range(k):
            if p2 == None:
                return None
            p2 = p2.next
        

        while p2.next!=None:
            p1=p1.next
            p2=p2.next
        return p1.data
        



if __name__=='__main__':
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.append(5)

    print(llist.getKthTolast(4))
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
    
    def deleteDuplicatesWithBuffer(self):
        itemCount = {}
        temp = self.head
        while temp!=None:
            if itemCount.get(temp.data)==None:
                itemCount[temp.data]=1
                prev=temp
            else:
                itemCount[temp.data]+=1    
                prev.next = temp.next
            temp = temp.next



if __name__=='__main__':
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(2)
    llist.append(1)
    llist.append(4)
    llist.append(5)
    llist.deleteDuplicatesWithBuffer()

    llist.printlist()
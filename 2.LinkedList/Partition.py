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
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            newNode= Node(data)
            newNode.next = self.head
            self.head = newNode
                
    def printlist(self):
        temp = self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next

def partition(linkedList, partitionAt):
    paritionedLl = LinkedList()

    temp = linkedList.head
    while temp!=None:
        if temp.data>=partitionAt:
            paritionedLl.append(temp.data)
        else:
            paritionedLl.push(temp.data)
        temp = temp.next
    
    return paritionedLl

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(5)
    ll.append(8)
    ll.append(5)
    ll.append(10)
    ll.append(12)
    ll.append(1)
    ll.append(2)

    partitionedLinkedList = partition(ll, 2)

    partitionedLinkedList.printlist()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
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

def findCollision(ll):
    slow = ll.head 
    fast = ll.head
    
    while 1:
        slow = slow.next
        fast = fast.next.next

        if(slow == fast):
            break
    slow = ll.head        
    while slow!=fast:
        slow = slow.next
        fast = fast.next

    print(slow.data)


if __name__ == "__main__":
    ll = LinkedList()

    e = Node("e")

    ll.appendNode(Node("a"))
    ll.appendNode(Node("b"))
    ll.appendNode(Node("c"))
    ll.appendNode(Node("d"))
    ll.appendNode(e)
    ll.appendNode(Node("f"))
    ll.appendNode(Node("g"))
    ll.appendNode(Node("h"))
    ll.appendNode(Node("i"))
    ll.appendNode(Node("j"))
    ll.appendNode(e)

    findCollision(ll)
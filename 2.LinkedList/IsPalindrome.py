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

    def push(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            newNode= Node(data)
            newNode.next = self.head
            self.head = newNode

def reverse(node):
    reversedLinkedList = LinkedList()
    
    while node!=None:
        reversedLinkedList.push(node.data)
        node = node.next
    
    return reversedLinkedList


def isPalindrome(ll1, ll2):

    l1head = ll1.head
    l2head = ll2.head

    while l1head!=None and l2head !=None:
        if l1head.data != l2head.data:
            return False
        l1head = l1head.next
        l2head = l2head.next
    return True


        



if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(2)
    ll.append(1)

    llr = reverse(ll.head)

    print(isPalindrome(ll, llr))
    
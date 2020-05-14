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

def sumList(list1, list2):
    summedList = LinkedList()

    carry = 0

    temp1 = list1.head
    temp2 = list2.head

    while temp1!=None:

        total = temp1.data + temp2.data + carry  
        res = total % 10
        carry = int( total / 10) 

        summedList.append(res)

        temp1 = temp1.next
        temp2 = temp2.next

    summedList.printlist()

if __name__ == "__main__":
    list1 = LinkedList()
    list2 = LinkedList()

    list1.append(7)
    list1.append(1)
    list1.append(6)

    list2.append(5)
    list2.append(9)
    list2.append(2)

    sumList(list1, list2)
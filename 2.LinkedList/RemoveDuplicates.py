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


    def deleteNode(self, nodeVal):
        temp = self.head
        while temp!=None:
            if temp.data == nodeVal:
                prev.next  = temp.next    
                break
            prev = temp
            temp = temp.next

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
    
    def deleteDuplicatesWithBuffer(self):
        itemCount = {}
        temp = self.head
        while temp!=None:
            if itemCount.get(temp.data)==None:
                itemCount[temp.data]=1
                prev=temp
            else:
                print(itemCount,temp.data, prev.data, temp.next.data)
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
    # llist.insertAfter(2,7)

    llist.deleteDuplicatesWithBuffer()

    llist.printlist()  

    #llist.deleteNode(3)
    
    # print(llist.getLn())
    # #llist.printlist()
    # # 
    # print(llist.search(12))       
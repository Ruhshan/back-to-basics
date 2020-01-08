
from doubly import DoublyLinkedList

if __name__=='__main__':
    dll = DoublyLinkedList()

    dll.append(0)
    dll.append(1)
    dll.append(2)
    dll.append(3)


    dll.delete(3)
    #dll.delete(10)

    dll.printList()

    dll.printReverse()

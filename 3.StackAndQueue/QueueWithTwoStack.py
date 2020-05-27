class BaseStack:
    def __init__(self):
        self.data = [None] * 30
        self.top = 0
    
    def push(self, item):
        self.data[self.top] = item
        self.top += 1
    
    def pop(self):
        self.top -= 1
        ret = self.data[self.top]
        self.data[self.top] = None

        return ret
    
    def isFull(self):
        return self.top == 3
    
    def isEmpty(self):
        return self.top == 0

class MyQueue:
    def __init__(self):
        self.forward = BaseStack()
        self.reverse = BaseStack()
    
    def enqueue(self, item):
        self.forward.push(item)
    
    def dequeue(self):
        if self.reverse.isEmpty():
            while not self.forward.isEmpty():
                self.reverse.push(self.forward.pop())
        return self.reverse.pop()

if __name__ == "__main__":
    myQueue = MyQueue()
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    myQueue.enqueue(4)

    print(myQueue.dequeue())
    print(myQueue.dequeue())
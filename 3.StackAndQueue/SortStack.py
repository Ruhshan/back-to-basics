class BaseStack:
    def __init__(self):
        self.data = [None] * 10
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

    def getTop(self):
        return self.data[self.top-1]


def sort(stack):
    tempStack = BaseStack()

    while not stack.isEmpty():
        tmp = stack.pop()
        if tempStack.getTop() > tmp:
            stack.push(tempStack.pop())
        tempStack.push(tmp)
    return tempStack



if __name__ == "__main__":
    mystack = BaseStack()

    mystack.push(98)
    mystack.push(32)
    mystack.push(12)
    mystack.push(34)
    mystack.push(3)
    mystack.push(120)

    sorted = sort(mystack)

    print(sorted.data)
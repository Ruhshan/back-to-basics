class BaseStack:
    def __init__(self):
        self.data = [None] * 3
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

class PlateStack:
    def __init__(self):
        self.stacks =[]
        self.last = None
    
    def push(self,item):
        if self.last == None or self.last.isFull():
            stack = BaseStack()
            self.stacks.append(stack)
            self.last = stack

            self.last.push(item)
        else:
            self.last.push(item)
    
    def pop(self):
        ret = self.last.pop()

        if self.last.isEmpty():
            del self.stacks[-1]
            self.last = self.stacks[-1]

        return ret

    def printAll(self):
        for s in self.stacks:
            print(s.data)


if __name__ == "__main__":
    plateStack = PlateStack()

    plateStack.push(1)
    plateStack.push(1)
    plateStack.push(1)
    plateStack.push(1)
    plateStack.push(1)
    plateStack.push(1)
    


    plateStack.printAll()

    print("-------")
    plateStack.pop()
    plateStack.pop()
    

    plateStack.printAll()




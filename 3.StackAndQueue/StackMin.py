class StackMin:
    def __init__(self, n):
        self.min = 999999999
        self.data = [None] * n
        self.top = 0
        self.minstack = []
    
    def push(self, item):
        self.data[self.top] = item
        self.top += 1

        if item < self.min:
            self.min = item
            self.minstack.append(self.min)

    def pop(self):
        self.top -= 1
        ret = self.data[self.top]

        if ret == self.min:
            self.minstack.pop()
            self.min = self.minstack[-1]

        return ret

    def printAll(self):
        print("Top : ", self.top)
        print("Array : ", self.data)
        print("Min : ", self.min)
        print("Minstack ", self.minstack)
        


if __name__ == "__main__":
    s = StackMin(10)

    s.push(18)
    s.push(20)
    s.push(2)
    s.push(3)

    s.printAll()

    print("popped ",s.pop())
    print("popped ", s.pop())

    s.printAll()


         
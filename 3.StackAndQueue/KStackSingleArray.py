class KStack:
    def __init__(self,k,n):
        self.top = [-1]*k
        self.array = [0]*n
        self.free = 0
        self.next = [i for i in range(1, n+1)]
    
    def push(self, stk, itm):
        self.array[self.free] = itm

        top_tmp = self.top[stk]
        next_tmp = self.next[self.free]

        self.next[self.free] = top_tmp
        self.top[stk] = self.free
        
        self.free = next_tmp

    
    def pop(self, stk):
        result = self.array[self.top[stk]]

        current_top = self.top[stk]
        
        self.top[stk] =  self.next[current_top]
        self.next[current_top] = self.free
        self.free = current_top

        return result


    def printAll(self):
        print("Top : ", self.top)
        print("Array : ", self.array)
        print("Next : ", self.next)
        print("Free : ", self.free)


if __name__ == "__main__":
    stack = KStack(3, 12) 
    stack.push(0, 5)
    stack.push(0, 6)
    stack.push(0, 7)

    stack.printAll()

    print(stack.pop(0))
    stack.push(0, 8)
    stack.push(0, 9)

    stack.printAll()  
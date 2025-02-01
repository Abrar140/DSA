class Stack:
    def __init__(self, size):
        self.stack=[None]*size
        self.top=-1
        self.size=size
    
    def push(self, value):
        if self.top==self.size-1:
            print ("Stack is full")
        else:
            self.top+=1
            self.stack[self.top]=value

    def pop(self):
        if self.top==-1:
            print("Stack is empty")
        else:
            value =self.stack[self.top]
            self.stack[self.top]=None
            self.top-=1
            return value
          
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return None
        else:
            return self.stack[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

    def size(self):
        return self.top + 1

    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack elements:", self.stack[:self.top + 1])


# Example usage:
stack = Stack(5)
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.pop()
print("Top element:", stack.peek())
stack.display()

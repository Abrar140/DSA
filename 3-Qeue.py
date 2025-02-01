class Queue:
    def __init__(self,size):
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
        self.capacity=size
    
    def enqueue(self, value):
        if self.rear==self.capacity-1:
            print("Qeueue is filled")
        else:
            if self.front==-1:
                self.front=0
            self.rear+=1
            self.queue[self.rear]=value
    
    def dequeue(self):
        if self.front==-1:
            print("Qeueue is empty")
        else:
            value=self.queue[self.front]
            self.queue[self.front]=None
            self.front+=1
            if self.front>self.rear:
                self.front=self.rear=-1
            return value

    def peek(self):
        if self.isEmpty():
            print("Qeue is empty")
            return None
    
        return   self.queue[self.front]

    def isEmpty(self):
        return self.front==-1 or self.front>self.rear

    def isFull(self):  
        return self.rear==self.size-1

    def size(self):
        if self.isEmpty():
            return 0
        return self.rear-self.front+1

    def display(self):
        if self.isEmpty():
            print("Qeueue is empty")
        else:
            print("Qeueue elements:", self.queue[:self.rear + 1])

           



q=Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.display()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()

q.display()
print("Top element:", q.peek())
q.dequeue()
q.display()
q.enqueue(1)
q.display()
    

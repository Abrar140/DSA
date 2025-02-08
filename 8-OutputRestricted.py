class OutputRestrictedQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        self.capacity = size
    
    def enqueue_rear(self, value):
        if self.rear == self.capacity - 1:
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = value
    
    def enqueue_front(self, value):
        if self.front == 0:
            print("Cannot enqueue at front")
        else:
            if self.front == -1:
                self.front = self.rear = 0
            else:
                self.front -= 1
            self.queue[self.front] = value
    
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            value = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            if self.front > self.rear:
                self.front = self.rear = -1
            return value
    
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.queue[self.front]
    
    def isEmpty(self):
        return self.front == -1 or self.front > self.rear
    
    def isFull(self):  
        return self.rear == self.capacity - 1
    
    def size(self):
        if self.isEmpty():
            return 0
        return self.rear - self.front + 1
    
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue elements:", self.queue[self.front:self.rear + 1])


q = OutputRestrictedQueue(5)
q.enqueue_rear(10)
q.enqueue_rear(20)
q.enqueue_front(5)
q.enqueue_rear(30)
q.enqueue_rear(40)
q.display()
q.dequeue()
q.display()
q.enqueue_front(2)
q.display()

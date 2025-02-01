class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity  # Array of fixed size
        self.front = 0  # Front index
        self.size = 0   # Current number of elements
        self.capacity = capacity  # Max size

    def enqueue(self, value):
        if self.isFull():
            print("Queue is full")
            return
        
        rear = (self.front + self.size) % self.capacity  # Calculate rear index   
        self.queue[rear] = value
        self.size += 1  # Increment size

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        
        value = self.queue[self.front]  # Get front value
        self.queue[self.front] = None  # Mark position as empty
        self.front = (self.front + 1) % self.capacity  # Move front forward
        self.size -= 1  # Decrement size
        
        return value

    def getFront(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def getRear(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        rear_index = (self.front + self.size - 1) % self.capacity
        return self.queue[rear_index]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def getSize(self):
        return self.size

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue state:", self.queue)
            # elements = []
            # for i in range(self.size):
            #     elements.append(self.queue[(self.front + i) % self.capacity])
            # print("Queue elements:", elements)


# Testing Circular Queue
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.display()  # [10, 20, 30, 40, 50]

cq.dequeue()  # Removes 10
cq.display()  # [None, 20, 30, 40, 50]

print("Front:", cq.getFront())  # 20
print("Rear:", cq.getRear())  # 50

cq.enqueue(60)  # 60 should be inserted at index 0
cq.display()  # [60, 20, 30, 40, 50]

cq.dequeue()  # Removes 20
cq.display()  # [60, None, 30, 40, 50]

cq.enqueue(70)  # Should replace index 1
cq.display()  # [60, 70, 30, 40, 50]

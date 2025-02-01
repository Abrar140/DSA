class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.deque = [None] * capacity  # fixed-size list to hold elements
        self.front = -1  # index of front element
        self.rear = -1   # index of rear element

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        # The deque is full if front is right after rear in a circular manner.
        return (self.front == 0 and self.rear == self.capacity - 1) or (self.front == self.rear + 1)

    def enqueue_front(self, value):
        if self.isFull():
            print("Deque is full. Cannot insert at front.")
            return

        # If the deque is empty, initialize front and rear to 0.
        if self.isEmpty():
            self.front = self.rear = 0
        elif self.front == 0:
            self.front = self.capacity - 1  # wrap-around to the end of array
        else:
            self.front -= 1

        self.deque[self.front] = value

    def enqueue_rear(self, value):
        if self.isFull():
            print("Deque is full. Cannot insert at rear.")
            return

        if self.isEmpty():
            self.front = self.rear = 0
        elif self.rear == self.capacity - 1:
            self.rear = 0  # wrap-around to the beginning of array
        else:
            self.rear += 1

        self.deque[self.rear] = value

    def dequeue_front(self):
        if self.isEmpty():
            print("Deque is empty. Cannot dequeue from front.")
            return None

        value = self.deque[self.front]
        self.deque[self.front] = None  # Optional: Clear the slot

        # If the deque had only one element, reset it to empty state.
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.capacity - 1:
            self.front = 0
        else:
            self.front += 1

        return value

    def dequeue_rear(self):
        if self.isEmpty():
            print("Deque is empty. Cannot dequeue from rear.")
            return None

        value = self.deque[self.rear]
        self.deque[self.rear] = None  # Optional: Clear the slot

        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.rear == 0:
            self.rear = self.capacity - 1
        else:
            self.rear -= 1

        return value

    def peek_front(self):
        if self.isEmpty():
            print("Deque is empty.")
            return None
        return self.deque[self.front]

    def peek_rear(self):
        if self.isEmpty():
            print("Deque is empty.")
            return None
        return self.deque[self.rear]

    def display(self):
        if self.isEmpty():
            print("Deque is empty.")
            return

        print("Deque elements:", end=" ")
        i = self.front
        while True:
            print(self.deque[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()


# Example usage:
dq = Deque(5)

print("Enqueue at rear: 10, 20, 30")
dq.enqueue_rear(10)
dq.enqueue_rear(20)
dq.enqueue_rear(30)
dq.display()

print("Enqueue at front: 5")
dq.enqueue_front(5)
dq.display()

print("Peek front:", dq.peek_front())
print("Peek rear:", dq.peek_rear())

print("Dequeue from front:", dq.dequeue_front())
dq.display()

print("Dequeue from rear:", dq.dequeue_rear())
dq.display()

print("Enqueue at rear: 40")
dq.enqueue_rear(40)
dq.display()

print("Enqueue at front: 2")
dq.enqueue_front(2)
dq.display()


class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity  # fixed-size list
        self.size = 0  # number of current elements

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.isFull():
            print("Queue is full")
        else:
            self.queue[self.size] = value
            self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            # Find the index of the smallest element
            min_index = 0
            for i in range(1, self.size):
                if self.queue[i] < self.queue[min_index]:
                    min_index = i
            
            min_value = self.queue[min_index]
            
            # Remove the element by shifting the remaining elements left
            for i in range(min_index, self.size - 1):
                self.queue[i] = self.queue[i + 1]
            self.queue[self.size - 1] = None
            self.size -= 1
            
            return min_value

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            # Find the smallest element without removing it
            min_value = self.queue[0]
            for i in range(1, self.size):
                if self.queue[i] < min_value:
                    min_value = self.queue[i]
            return min_value

    def get_size(self):
        return self.size

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            # Only display the active part of the queue
            print("Queue elements:", self.queue[:self.size])

# Example usage:
q = PriorityQueue(5)
q.enqueue(50)
q.enqueue(20)
q.enqueue(90)
q.enqueue(40)
q.enqueue(50)
q.display()

print("Dequeue (should remove the smallest):", q.dequeue())
print("Dequeue (should remove the next smallest):", q.dequeue())
q.display()
print("Peek (should show the smallest element):", q.peek())
q.enqueue(1)
q.display()

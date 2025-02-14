class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = new_node
            self.head.prev = new_node
            self.head = new_node
    
    def delete_node(self, key):
        if not self.head:
            return
        temp = self.head
        while temp.data != key:
            temp = temp.next
            if temp == self.head:
                return
        if temp.next == temp:
            self.head = None
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            if temp == self.head:
                self.head = temp.next
    
    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        last = None
        print("Forward: ", end="")
        while True:
            print(temp.data, end=" <-> ")
            last = temp
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")
        print("Backward: ", end="")
        while True:
            print(last.data, end=" <-> ")
            last = last.prev
            if last.next == self.head:
                break
        print("(tail)")

# Example usage
cdll = CircularDoublyLinkedList()
cdll.insert_at_end(10)
cdll.insert_at_end(20)
cdll.insert_at_end(30)
cdll.display()

cdll.insert_at_beginning(5)
cdll.insert_at_beginning(1)
cdll.display()

cdll.delete_node(20)
cdll.display()

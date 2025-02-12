class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

class DoubleLinkList:
    def __init__(self):
        self.head = None

    def insertlast(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        newnode.back = temp

    def insertstart(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode  # If list is empty, new node becomes the head
            return
        newnode.next = self.head
        self.head.back = newnode
        self.head = newnode

    def deletenode(self, key):
        temp = self.head

        # Case 1: If the head itself holds the key
        if temp and temp.data == key:
            self.head = temp.next  # Move head to the next node
            if self.head:  # If there's a new head, update its back pointer
                self.head.back = None
            temp = None
            return

        # Traverse to find the node to be deleted
        while temp and temp.data != key:
            temp = temp.next

        # If key not found
        if temp is None:
            return

        # Case 2: If the node to be deleted is the last node
        if temp.next is None:
            temp.back.next = None  # Simply update the previous node's next to None
            temp = None
            return

        # Case 3: If the node is in the middle
        temp.back.next = temp.next
        temp.next.back = temp.back  # Fix: Only update back pointer if next node exists

        temp = None  # Free the memory

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        
        temp = self.head
        last = None

        # Print forward traversal
        print("Forward: ", end="")
        while temp:
            print(temp.data, end=" <-> ")
            last = temp  # Store the last node
            temp = temp.next
        print("None")

        # Print backward traversal from last node
        print("Backward:", end=" ")
        while last:
            print(last.data, end=" <-> ")
            last = last.back
        print("None")


# Creating a linked list object
ll = DoubleLinkList()

# Inserting elements at the end
ll.insertlast(10)
ll.insertlast(20)
ll.insertlast(30)

# Displaying the linked list
print("Linked List after inserting at end:")
ll.display()

# Inserting elements at the beginning
ll.insertstart(5)
ll.insertstart(1)

# Displaying the linked list
print("Linked List after inserting at start:")
ll.display()

# Deleting a node
ll.deletenode(20)

# Displaying the linked list after deletion
print("Linked List after deleting node with value 20:")
ll.display()

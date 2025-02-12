class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def insertlast(self,data):
        newnode= Node(data)
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode

    def insertstart(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

    def deletenode(self,key):
        temp=self.head
        if temp and temp.data==key:
            self.head=temp.next
            temp=None
            return
        prev=None
        while temp and temp.data!=key:
            prev=temp
            temp=temp.next
        if temp is None:
            return
        prev.next=temp.next
        temp=None
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")



# Creating a linked list object
ll = LinkList()

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


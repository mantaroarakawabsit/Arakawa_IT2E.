# Singly Linked List Program

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def remove_first(self):
        if self.head is not None:
            self.head = self.head.next

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


name = "ARAKAWA"
linked_list = LinkedList()

# Add each letter
for letter in name:
    linked_list.append(letter)

print("Linked List:")
linked_list.display()

# Remove each letter until empty
while linked_list.head is not None:
    linked_list.remove_first()
    linked_list.display()

print("Linked List is empty.")
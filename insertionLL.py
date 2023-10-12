class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0
            while current and count < position - 1:
                current = current.next
                count += 1
            if current is None:
                print("Position is out of range.")
            else:
                new_node.next = current.next
                current.next = new_node

# Create a linked list
my_linked_list = LinkedList()

# Append elements to the linked list
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

# Display the contents of the linked list
my_linked_list.display()

# Insert an element at a specific position
my_linked_list.insert_at_position(5, 2)

# Display the updated linked list
my_linked_list.display()

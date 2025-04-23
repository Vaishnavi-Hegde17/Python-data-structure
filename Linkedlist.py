class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to next node

class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    def add(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If list is empty, make new node the head
        else:
            current = self.head
            while current.next:
                current = current.next  # Traverse to the end
            current.next = new_node  # Link new node at the end

   

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
ll = LinkedList()
ll.add(10)
ll.add(20)
ll.display()
ll.add(30)
ll.display()  

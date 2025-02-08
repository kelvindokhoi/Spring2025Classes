class Node:
    def __init__(self, v):
        self.var = v
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def addtoHead(self, v):
        newNode = Node(v)
        if self.head is None:  # Empty deque
            self.head = newNode
            self.tail = newNode
        else:  # Non-empty deque
            newNode.next = self.head  # Connect new node's 'next' to the old head
            self.head.prev = newNode  # Connect old head's 'prev' to the new node
            self.head = newNode        # Update the deque's head to the new node

    # ... other Deque methods ...

# Example usage (add a print method for testing)
    def print_deque(self):
        current = self.head
        while current:
            print(current.var, end=" ")
            current = current.next
        print()


my_deque = Deque()
my_deque.addtoHead(1)
my_deque.addtoHead(2)
my_deque.addtoHead(3)
my_deque.print_deque()  # Output: 3 2 1
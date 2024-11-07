# Exercise 6 --> Detect Loop in Linked List: Write a function to detect if a linked list has a cycle.

# Floyd's Cycle-Finding Algorithm

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def detect_loop(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
    
linked_list = LinkedList()
linked_list.push(5)
linked_list.push(4)
linked_list.push(3)
linked_list.push(2)
linked_list.push(1)
linked_list.push(0)

print("Linked List: ")
linked_list.print_list()

# Detect Loop
print("Any Loops? ", linked_list.detect_loop())

# TEST
linked_list.head.next.next.next.next = linked_list.head.next

# Detect Loop After TEST

print("Any Loops after TEST? ", linked_list.detect_loop())

# OUTPUT

'''

Linked List: 
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None
Any Loops?  False
Any Loops after TEST?  True

'''

# Exercise 5 --> Reverse a Linked List: Implement a function to reverse a singly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
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

# REVERSE
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

linked_list = LinkedList()
linked_list.push(5)
linked_list.push(4)
linked_list.push(3)
linked_list.push(2)
linked_list.push(1)
linked_list.push(0)

print("Linked List: ") 
linked_list.print_list()

linked_list.reverse()

print("Reverse Linked List: ")
linked_list.print_list()

# OUTPUT

'''

Linked List: 
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None
Reverse Linked List: 
5 -> 4 -> 3 -> 2 -> 1 -> 0 -> None

'''

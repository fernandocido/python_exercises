# Exercise 8 --> Find N-th Node from End: Implement a function to find the n-th node from the end of a linked list.

# two-pointer approach

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

    def printed_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def find_nth_from_end(self, n):
        first = self.head
        second = self.head

        # first pointer
        for _ in range(n):
            if first is None:
                return None
            first = first.next

        # both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next

        return second.data if second else None  
    
linked_list = LinkedList()
linked_list.push(10)
linked_list.push(20)
linked_list.push(30)
linked_list.push(40)
linked_list.push(50)

print("Linked List: ")
linked_list.printed_list()

# example
n = 2
result = linked_list.find_nth_from_end(n)
print(f"The {n}-th node from the end is: {result}")

# OUTPUT

'''

Linked List: 
50 -> 40 -> 30 -> 20 -> 10 -> None
The 2-th node from the end is: 20

'''
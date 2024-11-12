# Exercise 7 --> Merge Two Sorted Linked Lists: Given two sorted linked lists, merge them into one sorted linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push (self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
            print("None")

    @staticmethod
    def merged_sorted_lists(list1, list2):
        dummy = Node(0)
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1 is not None:
            tail.next = list1
        elif list2 is not None:
            tail.next = list2

        return dummy.next

list1 = LinkedList()
list1.push(10)
list1.push(8)
list1.push(6)
list1.push(4)
list1.push(2)

list2 = LinkedList()
list2.push(9)
list2.push(7)
list2.push(5)
list2.push(3)
list2.push(1)

print("List1: ")
list1.print_list()

print("List2: ")
list2.print_list()

merged_head = LinkedList.merged_sorted_lists(list1.head, list2.head)

print("Merged List: ")
current = merged_head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# OUTPUT

'''

List1: 
2 -> None
4 -> None
6 -> None
8 -> None
10 -> None
List2: 
1 -> None
3 -> None
5 -> None
7 -> None
9 -> None
Merged List: 
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> None

'''

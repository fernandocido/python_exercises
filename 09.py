# Exercise 9 --> Implement Stack with Arrays: Create a stack using an array and implement push, pop, and peek operations.

class Stack:
    def __init__(self):
        # Internal array to store stack elements
        self.stack = []  

    def push(self, item):
        # Add an item to the top of the stack
        self.stack.append(item)

    def pop(self):
        # Remove and return the top item of the stack
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def peek(self):
        # Return the top item without removing it
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def size(self):
        # Return the number of items in the stack
        return len(self.stack)

# Create a stack instance
my_stack = Stack()

# Push items onto the stack
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Peek the top item
print("Top of stack (peek):", my_stack.peek())

# Pop items from the stack
print("Popped item:", my_stack.pop())
print("Popped item:", my_stack.pop())

# Check if the stack is empty
print("Is stack empty?", my_stack.is_empty())

# Check the size of the stack
print("Stack size:", my_stack.size())

# Pop the last item
print("Popped item:", my_stack.pop())

# OUTPUT

'''

Top of stack (peek): 30
Popped item: 30
Popped item: 20
Is stack empty? False
Stack size: 1
Popped item: 10

'''

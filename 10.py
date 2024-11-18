# Exercise 10 --> Balanced Parentheses Checker: Check if a given expression has balanced parentheses using a stack.

def is_balanced(expression):
    # Mapping of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in expression:
        # Opening brackets
        if char in bracket_map.values():
            stack.append(char)
        # Closing brackets
        elif char in bracket_map.keys():
            if not stack or stack.pop() != bracket_map[char]:
                return False

    # If the stack is empty, all brackets were balanced
    return len(stack) == 0

# Test
expressions = [
    "()",
    "([])",
    "{[()]}",
    "([)]",
    "((())",
    "{[()]}"
]

for expr in expressions:
    print(f"{expr}: {'Balanced' if is_balanced(expr) else 'Unbalanced'}")

# OUTPUT

'''

(): Balanced
([]): Balanced
{[()]}: Balanced
([)]: Unbalanced
((()): Unbalanced
{[()]}: Balanced

'''

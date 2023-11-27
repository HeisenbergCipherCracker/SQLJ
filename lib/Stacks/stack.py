from collections import deque
import sys
import os

current_directory = os.getcwd()
sys.path.append(current_directory)
from Exceptions.exceptions import SQLJNGStackOverflow


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, item, *args, **kwargs):
        self.stack.append(item)
        self.stack.extend(args)
        self.stack.extend(kwargs)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display_all(self):
        print("Captures:", list(self.stack))

# Example usage
html_response = Stack()
Significant_captures = Stack()

# s = Stack()
# s.push("t", "y")

# # Display all elements in the stack
# s.display_all()

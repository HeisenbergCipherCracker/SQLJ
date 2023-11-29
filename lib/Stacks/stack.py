from collections import deque

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

    def __iter__(self):
        self.current_index = len(self.stack) - 1
        return self

    def __next__(self):
        if self.current_index >= 0:
            result = self.stack[self.current_index]
            self.current_index -= 1
            return result
        else:
            raise StopIteration
        
    def __getitem__(self, index):
        return self.stack[index]
    
    def Insert_to_stack(self,indx,value):
        self.stack.insert(indx,value)

    def sort_stack(self):
        self.stack = deque(sorted(self.stack))

    def _binary_search_recursive(self, target, low, high):
        if low <= high:
            mid = (low + high) // 2
            if self.stack[mid] == target:
                return mid  # Return the index where the target was found
            elif self.stack[mid] < target:
                # Recursively search the right half
                return self._binary_search_recursive(target, mid + 1, high)
            else:
                # Recursively search the left half
                return self._binary_search_recursive(target, low, mid - 1)
        else:
            return None  # Return None if the target was not found

    def binary_search(self, target):
        self.sort_stack()  # Sort the stack before performing binary search
        return self._binary_search_recursive(target, 0, len(self.stack) - 1)

# Example usage
Significant_captures = Stack()
html_response = Stack()

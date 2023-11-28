import os
import sys

current_directory = os.getcwd()

sys.path.append(current_directory)
from lib.Stacks.stack import Stack


def binary_search(iterable, target):
    arr = list(iterable)  # Convert iterable to a list
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found in the iterable


sample = Stack()
sample.push(3, 5, 6, 7, 8, 5)
sample.display_all()

res = binary_search(sample,3)
print(res)


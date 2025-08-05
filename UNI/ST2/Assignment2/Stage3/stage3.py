import bisect

# 1. Design an ADT over Value Ranges
class InRange:
    def __init__(self, data):
        self.data = data  # data will be a list of values (can be sorted or unsorted)

    def search_range(self, lower, upper):
        """
        Searches for all values within the specified range [lower, upper]
        using linear or binary search depending on the underlying data structure.
        """
        raise NotImplementedError("Subclasses should implement this method.")

# 2. Implement ADT for Unordered Lists (Linear Search)
class UnorderedInRange(InRange):
    def search_range(self, lower, upper):
        return [value for value in self.data if lower <= value <= upper]

# 3. Implement ADT for Sorted Lists (Binary Search)
class SortedInRange(InRange):
    def search_range(self, lower, upper):
        # Using bisect to find insertion points for binary search
        left_index = bisect.bisect_left(self.data, lower)
        right_index = bisect.bisect_right(self.data, upper)
        return self.data[left_index:right_index]

# 4. Implement a Stack (for temporary data management during search)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

# 5. Implement ADT for Binary Search Trees (BSTs)
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert(node.right, value)

    def search_range(self, lower, upper):
        result = self._search_range(self.root, lower, upper)
        return sorted(result)  # Sort the results before returning them

    def _search_range(self, node, lower, upper):
        if node is None:
            return []

        result = []
        if lower <= node.value <= upper:
            result.append(node.value)

        if node.value > lower:
            result.extend(self._search_range(node.left, lower, upper))

        if node.value < upper:
            result.extend(self._search_range(node.right, lower, upper))

        return result

# 6. Read in a CSV File (for real estate data)
import csv

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            data.append([float(x) for x in row])  # Assume values are numerical
    return data

# 7. Implement Loading Functionality
def load_data(filename, data_structure):
    data = read_csv(filename)
    for row in data:
        for value in row:
            data_structure.insert(value)
    return data_structure

# 8. Implement Driver Loop (Interactive Command Loop)
def driver_loop():
    bst = BinarySearchTree()
    data_structure = SortedInRange([10, 20, 30, 40, 50, 60, 70])  # Example data

    while True:
        command = input("Enter command (search range, quit): ")
        if command.lower() == "quit":
            break
        elif command.startswith("search"):
            _, lower, upper = command.split()
            lower, upper = int(lower), int(upper)
            results = data_structure.search_range(lower, upper)
            print(f"Found values: {results}")
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    driver_loop()

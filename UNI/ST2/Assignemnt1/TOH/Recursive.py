def recursive_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    recursive_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    recursive_hanoi(n - 1, auxiliary, target, source)


# Iterative Algorithm using Stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0
    
if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))

    print("\nRecursive Solution:")
    recursive_hanoi(n, 'A', 'C', 'B')

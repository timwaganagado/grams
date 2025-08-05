# Recursive Algorithm
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


def iterative_hanoi(n, source, target, auxiliary):
    stack = Stack()
    stack.push((n, source, target, auxiliary))

    while not stack.is_empty():
        disk, src, tgt, aux = stack.pop()
        if disk == 1:
            print(f"Move disk 1 from {src} to {tgt}")
        else:
            stack.push((disk - 1, aux, tgt, src))
            stack.push((1, src, tgt, aux))
            stack.push((disk - 1, src, aux, tgt))


# Example usage
if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))

    print("\nRecursive Solution:")
    recursive_hanoi(n, 'A', 'C', 'B')

    print("\nIterative Solution:")
    iterative_hanoi(n, 'A', 'C', 'B')

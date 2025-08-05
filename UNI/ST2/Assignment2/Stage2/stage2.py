import csv
import os
import sys
import time
from abc import ABC, abstractmethod

class ListADT(ABC):
    @abstractmethod
    def insert(self, item): pass

    @abstractmethod
    def get(self, index): pass

    @abstractmethod
    def set(self, index, item): pass

    @abstractmethod
    def length(self): pass

    @abstractmethod
    def to_list(self): pass

class PythonList(ListADT):
    def __init__(self):
        self.data = []

    def insert(self, item):
        self.data.append(item)

    def get(self, index):
        return self.data[index]

    def set(self, index, item):
        self.data[index] = item

    def length(self):
        return len(self.data)

    def to_list(self):
        return self.data

def merge_sort(lst, key_index):
    if lst.length() <= 1:
        return lst

    mid = lst.length() // 2
    left = PythonList()
    right = PythonList()

    for i in range(mid):
        left.insert(lst.get(i))
    for i in range(mid, lst.length()):
        right.insert(lst.get(i))

    return merge(merge_sort(left, key_index), merge_sort(right, key_index), key_index)

def merge(left, right, key_index):
    result = PythonList()
    i = j = 0

    while i < left.length() and j < right.length():
        try:
            left_val = float(left.get(i)[key_index])
        except:
            left_val = float('inf')
        try:
            right_val = float(right.get(j)[key_index])
        except:
            right_val = float('inf')

        if left_val <= right_val:
            result.insert(left.get(i))
            i += 1
        else:
            result.insert(right.get(j))
            j += 1

    while i < left.length():
        result.insert(left.get(i))
        i += 1
    while j < right.length():
        result.insert(right.get(j))
        j += 1

    return result

# === CSV Utils ===
def read_csv(filename):
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = list(reader)
    return header, rows

def write_csv(filename, header, data):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

# === Main Driver ===
def main():
    if len(sys.argv) != 4:
        print("Usage: python stage2.py <input_csv_file> <output_csv_file> <sort_column>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    sort_column = sys.argv[3]

    print(f"Reading from {input_file}...")
    header, rows = read_csv(input_file)

    key_index = header.index(sort_column)

    lst = PythonList()
    for row in rows:
        lst.insert(row)

    print(f"Sorting by column '{sort_column}'...")
    start = time.time()
    sorted_list = merge_sort(lst, key_index)
    end = time.time()

    print(f"Sorting complete in {end - start:.4f} seconds.")
    print(f"Writing sorted data to {output_file}...")
    write_csv(output_file, header, sorted_list.to_list())
    print("Done.")

if __name__ == "__main__":
    main()

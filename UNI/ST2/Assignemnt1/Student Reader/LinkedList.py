import os
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        print("\nStudent Data:")
        while current:
            student = current.data
            print(f"Name: {student['name']}, Grade: {student['grade']}, Age: {student['age']}, Gender: {student['gender']}, Level: {student['level']}")
            current = current.next


def read_student_data(filename):
    """Reads student data from a file and stores it in a linked list."""
    student_list = LinkedList()
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip().split(', '))
            name, grade, age, gender, level = line.strip().split(', ')
            if int(grade) > 50:
                if gender == "Male":
                    student_list.append({'name': name,'grade': int(grade),'age': int(age)+2,'gender': gender,'level': level})
                else:
                    student_list.append({'name': name,'grade': int(grade),'age': int(age)-2,'gender': gender,'level': level})
    return student_list



if __name__ == "__main__":
    filename = '/students.txt'
    filename = os.path.dirname(sys.argv[0]) + filename
    student_list = read_student_data(filename)
    student_list.display()
import sys
import os

def read_student_data(filename):
    """Reads student data from a file and prints each student's details."""
    try:
        with open(filename, 'r') as file:
            students = []
            for line in file:
                name, grade, age, gender, level = line.strip().split(', ')
                students.append({
                    'name': name,
                    'grade': int(grade),
                    'age': int(age),
                    'gender': gender,
                    'level': level
                })
            return students
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []


def display_students(students):
    """Displays the list of students."""
    print("\nStudent Data:")
    for student in students:
        print(f"Name: {student['name']}, Grade: {student['grade']}, Age: {student['age']}, Gender: {student['gender']}, Level: {student['level']}")


if __name__ == "__main__":
    filename = '/students.txt'
    filename = os.path.dirname(sys.argv[0]) + filename
    student_list = read_student_data(filename)
    display_students(student_list)
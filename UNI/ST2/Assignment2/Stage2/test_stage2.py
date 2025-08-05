import pytest
import os
import csv
from io import StringIO
from stage2 import PythonList, merge_sort, read_csv, write_csv

# Modify the read_csv to handle StringIO (file-like object)
def read_csv(file):
    reader = csv.reader(file)
    header = next(reader)
    rows = list(reader)
    return header, rows

# Modify the write_csv to handle StringIO (file-like object)
def write_csv(file, header, data):
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

# 1. Test the PythonList implementation
def test_python_list():
    python_list = PythonList()
    python_list.insert(['123', '1000000', '3', 'Melbourne'])
    python_list.insert(['124', '800000', '2', 'Brisbane'])
    python_list.insert(['125', '1200000', '4', 'Sydney'])

    assert python_list.get(0) == ['123', '1000000', '3', 'Melbourne']
    assert python_list.get(1) == ['124', '800000', '2', 'Brisbane']
    assert python_list.get(2) == ['125', '1200000', '4', 'Sydney']
    assert python_list.length() == 3

    python_list.set(0, ['123', '1100000', '3', 'Melbourne'])
    assert python_list.get(0) == ['123', '1100000', '3', 'Melbourne']

    assert python_list.to_list() == [
        ['123', '1100000', '3', 'Melbourne'],
        ['124', '800000', '2', 'Brisbane'],
        ['125', '1200000', '4', 'Sydney']
    ]


# 2. Test the merge_sort function
def test_merge_sort():
    unsorted_list = PythonList()
    unsorted_list.insert(['123', '1000000', '3', 'Melbourne'])
    unsorted_list.insert(['124', '800000', '2', 'Brisbane'])
    unsorted_list.insert(['125', '1200000', '4', 'Sydney'])

    sorted_list = merge_sort(unsorted_list, 1)

    assert sorted_list.get(0) == ['124', '800000', '2', 'Brisbane']
    assert sorted_list.get(1) == ['123', '1000000', '3', 'Melbourne']
    assert sorted_list.get(2) == ['125', '1200000', '4', 'Sydney']


# 3. Test the read_csv function with StringIO
def test_read_csv():
    csv_data = "Property_ID,Price,Rooms,Suburb\n123,1000000,3,Melbourne\n124,800000,2,Brisbane\n125,1200000,4,Sydney\n"
    file = StringIO(csv_data)  # Create a StringIO object to simulate file input
    header, rows = read_csv(file)

    assert header == ['Property_ID', 'Price', 'Rooms', 'Suburb']
    assert rows == [
        ['123', '1000000', '3', 'Melbourne'],
        ['124', '800000', '2', 'Brisbane'],
        ['125', '1200000', '4', 'Sydney']
    ]


# 4. Test the write_csv function with StringIO
def test_write_csv():
    output = StringIO()  # Use StringIO as the output file
    header = ['Property_ID', 'Price', 'Rooms', 'Suburb']
    data = [
        ['123', '1000000', '3', 'Melbourne'],
        ['124', '800000', '2', 'Brisbane'],
        ['125', '1200000', '4', 'Sydney']
    ]

    write_csv(output, header, data)

    # Verify that the content written to the StringIO object is correct
    output.seek(0)
    reader = csv.reader(output)
    rows = list(reader)

    assert rows == [
        ['Property_ID', 'Price', 'Rooms', 'Suburb'],
        ['123', '1000000', '3', 'Melbourne'],
        ['124', '800000', '2', 'Brisbane'],
        ['125', '1200000', '4', 'Sydney']
    ]


# 5. Integration Test (end-to-end test for reading, sorting, and writing CSV with StringIO)
def test_integration():
    csv_data = "Property_ID,Price,Rooms,Suburb\n123,1000000,3,Melbourne\n124,800000,2,Brisbane\n125,1200000,4,Sydney\n"
    input_file = StringIO(csv_data)
    header, rows = read_csv(input_file)

    lst = PythonList()
    for row in rows:
        lst.insert(row)

    sorted_list = merge_sort(lst, 1)

    output = StringIO()
    write_csv(output, header, sorted_list.to_list())

    output.seek(0)
    reader = csv.reader(output)
    rows = list(reader)

    assert rows == [
        ['Property_ID', 'Price', 'Rooms', 'Suburb'],
        ['124', '800000', '2', 'Brisbane'],
        ['123', '1000000', '3', 'Melbourne'],
        ['125', '1200000', '4', 'Sydney']
    ]


# Run the tests if this is the main module
if __name__ == "__main__":
    pytest.main()

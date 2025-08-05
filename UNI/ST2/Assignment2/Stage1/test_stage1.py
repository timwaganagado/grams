import pytest
import csv
import os
from tempfile import NamedTemporaryFile
from stage1 import read_csv, add_row  # Replace 'stage1' with the actual Python file name (without .py)

# ---------- FIXTURES AND HELPERS ----------

@pytest.fixture
def mock_csv_file():
    # Create a temporary CSV file
    headers = ['Property_ID', 'Suburb', 'Price']
    rows = [
        {'Property_ID': '101', 'Suburb': 'Melbourne', 'Price': '1000000'},
        {'Property_ID': '102', 'Suburb': 'Richmond', 'Price': '850000'}
    ]

    temp = NamedTemporaryFile(mode='w+', delete=False, newline='', suffix='.csv')
    writer = csv.DictWriter(temp, fieldnames=headers)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    temp.close()
    yield temp.name
    os.remove(temp.name)

# ---------- TEST CASES ----------

def test_read_csv(mock_csv_file):
    data = read_csv(mock_csv_file)
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]['Suburb'] == 'Melbourne'
    assert data[1]['Price'] == '850000'

def test_add_row():
    data = [
        {'Property_ID': '101', 'Suburb': 'Melbourne', 'Price': '1000000'}
    ]
    new_row = {'Property_ID': '103', 'Suburb': 'Hawthorn', 'Price': '1200000'}
    add_row(data, new_row)
    assert len(data) == 2
    assert data[-1]['Suburb'] == 'Hawthorn'
    assert data[-1]['Price'] == '1200000'

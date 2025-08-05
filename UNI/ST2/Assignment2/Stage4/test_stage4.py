import os
import csv
import pytest
from stage4 import HashMap, remove_duplicates

# --- 1. HashMap Tests ---

def test_hashmap_basic_set_and_get():
    hm = HashMap()
    hm.set("test_key", "value")
    assert hm.get("test_key") == "value"
    assert hm.contains("test_key") is True

def test_hashmap_key_not_found():
    hm = HashMap()
    assert hm.get("missing") is None
    assert hm.contains("missing") is False

def test_hashmap_overwrite_value():
    hm = HashMap()
    hm.set("key", "value1")
    hm.set("key", "value2")
    assert hm.get("key") == "value2"

# --- 2. Deduplication Tests ---

@pytest.fixture
def sample_csv(tmp_path):
    test_file = tmp_path / "sample.csv"
    rows = [
        {"Description": "Nice house", "Price": "1000000"},
        {"Description": "Nice house", "Price": "1000000"},  # duplicate
        {"Description": "Modern flat", "Price": "850000"},
        {"Description": "Beach house", "Price": "1200000"},
        {"Description": "Modern flat", "Price": "850000"},  # duplicate
    ]

    with open(test_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["Description", "Price"])
        writer.writeheader()
        writer.writerows(rows)

    return test_file

def test_remove_duplicates(tmp_path, sample_csv):
    output_file = tmp_path / "output.csv"
    remove_duplicates(str(sample_csv), str(output_file))

    with open(output_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Should keep only 3 unique descriptions
    descriptions = [row["Description"] for row in rows]
    assert len(descriptions) == 3
    assert "Nice house" in descriptions
    assert "Modern flat" in descriptions
    assert "Beach house" in descriptions

if __name__ == "__main__":
    pytest.main()
import pytest
from stage3 import UnorderedInRange, SortedInRange, BinarySearchTree

# Test data
unordered_data = [50, 20, 30, 70, 10, 60, 40]
sorted_data = [10, 20, 30, 40, 50, 60, 70]
bst_data = [50, 20, 30, 70, 10, 60, 40]

# Test UnorderedInRange
def test_unordered_in_range():
    unordered = UnorderedInRange(unordered_data)
    
    # Test searching a range that includes values
    result = unordered.search_range(20, 50)
    assert result == [50, 20, 30, 40]

    # Test searching a range that includes no values
    result = unordered.search_range(80, 100)
    assert result == []

# Test SortedInRange
def test_sorted_in_range():
    sorted_range = SortedInRange(sorted_data)
    
    # Test searching a range that includes values
    result = sorted_range.search_range(20, 50)
    assert result == [20, 30, 40, 50]

    # Test searching a range that includes no values
    result = sorted_range.search_range(80, 100)
    assert result == []

# Test BinarySearchTree
def test_bst_search_range():
    bst = BinarySearchTree()
    
    # Insert elements into the BST
    for value in bst_data:
        bst.insert(value)
    
    # Test searching a range that includes values
    result = bst.search_range(20, 50)
    assert result == [20, 30, 40, 50]

    # Test searching a range that includes no values
    result = bst.search_range(80, 100)
    assert result == []

# Additional test for the edge case: empty data
def test_empty_data_structures():
    empty_unordered = UnorderedInRange([])
    empty_sorted = SortedInRange([])
    empty_bst = BinarySearchTree()

    # Test searching a range in empty unordered list
    result = empty_unordered.search_range(20, 50)
    assert result == []

    # Test searching a range in empty sorted list
    result = empty_sorted.search_range(20, 50)
    assert result == []

    # Test searching a range in empty BST
    result = empty_bst.search_range(20, 50)
    assert result == []

if __name__ == "__main__":
    pytest.main()
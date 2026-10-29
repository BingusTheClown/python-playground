import pytest
from algorithms.searchAlgorithms import SearchAlgorithms


def test_linear_search_string_returns_true_when_string_exists():
    assert SearchAlgorithms.linearSearchString("test", ["hello", "world", "test"]) == True

def test_lineach_search_string_returns_false_when_no_string_exists():
    assert SearchAlgorithms.linearSearchString("test", ["hello", "world", "Dave"]) == False

def test_linear_search_provided_with_nonstring_array_returns_value_error():
    with pytest.raises(ValueError):
        SearchAlgorithms.linearSearchString("test", [1,2,3])

def test_linear_search_provided_with_nonstring_search_string_returns_value_error():
    with pytest.raises(ValueError):
        SearchAlgorithms.linearSearchString(42, ["hello", "world", "test"])
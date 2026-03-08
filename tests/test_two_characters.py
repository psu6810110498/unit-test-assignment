import pytest
from _6810110498.two_characters import two_characters

def test_two_chars_normal():
    assert two_characters("beabeefeab") == 5

def test_two_chars_simple():
    assert two_characters("aba") == 3
    assert two_characters("aaa") == 0

def test_two_chars_empty():
    assert two_characters("") == 0

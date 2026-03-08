import pytest
from _6810110498.alternating_characters import alternating_characters

def test_alternating_normal():
    assert alternating_characters("AAAA") == 3
    assert alternating_characters("BBBBB") == 4
    assert alternating_characters("ABABABAB") == 0
    assert alternating_characters("BABABA") == 0

def test_alternating_mixed():
    assert alternating_characters("AAABBB") == 4

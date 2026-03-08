import pytest
from _6810110498.grid_challenge import grid_challenge

def test_grid_yes():
    grid = ["abc", "ade", "efg"]
    assert grid_challenge(grid) == "YES"

def test_grid_no():
    grid = ["abc", "hjk", "mpq", "rtv"] # Sorted, this would be YES
    grid_no = ["ebacd", "fghij", "olmkn", "trpqs", "abcde"] # Column check: 'e' > 'a' at bottom
    assert grid_challenge(grid_no) == "NO"

def test_grid_simple():
    assert grid_challenge(["a"]) == "YES"
    assert grid_challenge(["ba", "ab"]) == "YES" # จัดแล้วเป็น aa, bb ซึ่ง YES

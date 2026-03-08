import pytest
from _6810110498.funny_string import funny_string

def test_funny_string_funny():
    assert funny_string("acxz") == "Funny"
    assert funny_string("bcxz") == "Not Funny"

def test_funny_string_edge():
    # เคสตัวอักษรน้อยๆ หรือเหมือนกันหมด
    assert funny_string("aaaa") == "Funny"

def test_funny_string_complex():
    assert funny_string("lmnop") == "Funny"

import pytest
from _6810110498.caesar_cipher import caesar_cipher

def test_caesar_normal():
    assert caesar_cipher("middle-Outz", 2) == "okffng-Qwvb"

def test_caesar_rotate():
    assert caesar_cipher("Always-Look-on-the-Bright-Side-of-Life", 5) == "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"

def test_caesar_wrap():
    # เทสการเลื่อนที่เกิน 26
    assert caesar_cipher("abc", 27) == "bcd"

from Lev_2 import lev

import pytest

def test_equal():
    assert lev("ДОРОГА", "ДОРОГА") == 0

def test_diff():
    assert lev("АЧХ", "УПЧХИ") == 3

def test_empty():
    assert lev("", "gspd") == 4

if __name__ == '__main__':
    pytest.main()

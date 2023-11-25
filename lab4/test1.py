import unittest
from Lev_2 import lev

class TestLevenshteinDistance(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(lev("ГОРОД", "ГОРОД"), 0)

    def test_diff(self):
        self.assertEqual(lev("ГОРОД", "ГОРЫ"), 2)

    def test_empty(self):
        self.assertEqual(lev("", "nkvd"), 4)

if __name__ == '__main__':
    unittest.main()

# test_binarysearch

from binarysearch import binarysearch as bs
import unittest

class TestBinarySearch(unittest.TestCase):
    def test_simple_search(self):
        array = [0, 1, 2, 3]
        for i in range(4):
            search = bs(array, i)
            self.assertEqual(search, i)

    def test_search_upper_edge(self):
        array = [4, 5, 12, 52, 111, 621, 2911]
        search = bs(array, 2911)
        self.assertEqual(search, 6)

    def test_search_lower_edge(self):
        array = [4, 5, 12, 52, 111, 621, 2911]
        search = bs(array, 4)
        self.assertEqual(search, 0)

    def test_empty_array(self):
        array = []
        search = bs(array, 4)
        self.assertEqual(search, -1)

    def test_invalid_target(self):
        array = [12, 21, 38, 40]
        search = bs(array, 52)
        self.assertEqual(search, -1)

if __name__ == '__main__':
    unittest.main()
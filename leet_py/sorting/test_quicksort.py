# test_quicksort

from quicksort import quicksort as qs
import unittest

class TestQuickSort(unittest.TestCase):
    def test_simple_merge(self):
        array = [4, 3, 2, 1]
        self.assertEqual(qs(array, 0, len(array) - 1), [1, 2, 3, 4])
        
    def test_simple_negatives(self):
        array = [12, -12, 12, -102]
        self.assertEqual(qs(array, 0, len(array) - 1), [-102, -12, 12, 12])

    def test_simple_floats(self):
        array = [19.0, -12.2, 12.151, -23.11]
        self.assertEqual(qs(array, 0, len(array) - 1), [-23.11, -12.2, 12.151, 19.0])

    def test_empty_array(self):
        array = []
        self.assertEqual(qs(array, 0, len(array) - 1), [])

if __name__ == '__main__':
    unittest.main()
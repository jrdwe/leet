# test_mergesort

from mergesort import mergesort as ms
import unittest

class TestMergeSort(unittest.TestCase):
    def test_simple_merge(self):
        array = [4, 3, 2, 1]
        ms(array)        

        self.assertEqual(array, [1, 2, 3, 4])
        
    def test_simple_negatives(self):
        array = [12, -12, 12, -102]
        ms(array)        

        self.assertEqual(array, [-102, -12, 12, 12])

    def test_simple_floats(self):
        array = [19.0, -12.2, 12.151, -23.11]
        ms(array)        

        self.assertEqual(array, [-23.11, -12.2, 12.151, 19.0])

    def test_empty_array(self):
        array = []
        ms(array)

        self.assertEqual(array, [])

if __name__ == '__main__':
    unittest.main()
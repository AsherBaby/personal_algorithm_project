import unittest
from radix_sort import radix_sort

class TestOfRadixSort(unittest.TestCase):

    def test_of_small_array(self):
        a = [
            '4PGC938',
            '2IYE230',
            '3CIO720',
            '2RLA629',]
        radix_sort(a)
        self.assertEqual(
            a,
            ['2IYE230', '2RLA629', '3CIO720', '4PGC938',])

if __name__ == '__main__':
    unittest.main()

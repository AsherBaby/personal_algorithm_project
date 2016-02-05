import unittest
from trie import Trie

class Test(unittest.TestCase):

    def setUp(self):
        self.t = Trie(26)
        t = self.t
        t.insert('by', 4)
        t.insert('sea', 6)
        t.insert('sells', 1)
        t.insert('shells', 3)
        t.insert('shore', 7)
        t.insert('she', 0)
        t.insert('the', 5)

    def test_of_get(self):
        t = self.t
        self.assertEqual(t.get('shells'), 3)
        self.assertEqual(t.get('she'), 0)
        self.assertEqual(t.get('him'), None)

    def test_of_keys_with_prefix(self):
        t = self.t
        self.assertEqual(
            t.keys_with_prefix('sh'),
            ['she', 'shells', 'shore'])
        self.assertEqual(t.num_keys_with_prefix('sh'), 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)

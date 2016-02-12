import unittest
from LRU import LRUCache

class TestOfLRUCache(unittest.TestCase):

    def test_of_size_1(self):
        lru = LRUCache(1)
        lru.set(2, 1)
        self.assertEqual(lru.get(2), 1)
        lru.set(3, 2)
        self.assertIsNone(lru.get(2))
        self.assertEqual(lru.get(3), 2)

    def test_of_size_2(self):
        lru = LRUCache(2)
        lru.set(2, 1)
        lru.set(1, 1)
        self.assertEqual(lru.get(2), 1)
        lru.set(4, 1)
        self.assertIsNone(lru.get(1))
        self.assertEqual(lru.get(2), 1)

if __name__ == '__main__':
    unittest.main()

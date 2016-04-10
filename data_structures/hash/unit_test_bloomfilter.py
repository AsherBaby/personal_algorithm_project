import unittest
from bloomfilter import BloomFilter


class TestBloomFilter(unittest.TestCase):

    def setUp(self):
        self.bf = BloomFilter(256)
        self.existing_strings = [
            'tiny', 'bloom', 'rate', 'back', 'apple', 'google',
            'dijkstra', 'limiter', 'url', 'travel', 'man',
            '2',
        ]
        for each in self.existing_strings:
            self.bf.insert(each)
        self.non_existing_strings = [
            'multi', 'short', 'path', 'components', 'connect',
            'unit', 'test',
        ]

    def test_of_bloomfilter(self):
        for each in self.existing_strings:
            self.assertTrue(self.bf.lookup(each))
        for each in self.non_existing_strings:
            # with small false positive, this will fail :)
            self.assertFalse(self.bf.lookup(each))

if __name__ == '__main__':
    unittest.main()

import unittest
from KMP import KMP

class Test(unittest.TestCase):

    def test_of_kmp(self):
        pattern = 'abb'
        text = 'abababb'
        kmp = KMP(pattern)
        self.assertEqual(kmp.search(text), text.find(pattern))

if __name__ == '__main__':
    unittest.main()

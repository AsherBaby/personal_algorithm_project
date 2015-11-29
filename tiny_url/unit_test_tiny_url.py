import unittest
from tiny_url import TinyURL

class TestTinyURL(unittest.TestCase):

    def test_generate(self):
        tiny_url = TinyURL()
        self.assertEqual(
            tiny_url.generate('aaa'), 0)

    def test_lookup(self):
        tiny_url = TinyURL()
        self.assertEqual(
            tiny_url.lookup(tiny_url.generate('bbb')), 'bbb')

if __name__ == '__main__':
    unittest.main()

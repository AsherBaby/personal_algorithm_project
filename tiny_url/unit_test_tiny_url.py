import unittest
from tiny_url import TinyURL

class TestTinyURL(unittest.TestCase):

    def test_generate(self):
        tiny_url = TinyURL()
        self.assertEqual(
            tiny_url.generate('aaa'), '0')

    def test_lookup(self):
        tiny_url = TinyURL()
        self.assertEqual(
            tiny_url.lookup(tiny_url.generate('bbb')), 'bbb')
        self.assertEqual(
            tiny_url.lookup('ccc'), None)

    def test_encode(self):
        tiny_url = TinyURL()
        self.assertEqual(
            tiny_url._encode(0), '0')
        self.assertEqual(
            tiny_url._encode(10), 'a')
        self.assertEqual(
            tiny_url._encode(62), '10')

if __name__ == '__main__':
    unittest.main()

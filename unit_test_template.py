import unittest
# import ... as ...

class TestSomePackage(unittest.TestCase):

    def test_of_some_function(self):
        self.assertEqual(
            max(1, 0), 1)

if __name__ == '__main__':
    unittest.main()

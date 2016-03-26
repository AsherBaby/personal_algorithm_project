import unittest
from linked_hash_map import LinkedHashMap


class TesLinkedHashMap(unittest.TestCase):


    def test_of_everything(self):
        ht = LinkedHashMap()
        ht.insert(0, 'a')
        ht.insert(25, 'z')
        self.assertEqual(ht.get(0), 'a')
        self.assertEqual(ht.get(25), 'z')
        ht.remove(0)
        self.assertIsNone(ht.get(0))


if __name__ == '__main__':
    unittest.main()

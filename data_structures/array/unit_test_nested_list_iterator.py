import unittest
from nested_list_iterator import NestedIterator


class TestNestedIterator(unittest.TestCase):

    def test_of_bloomfilter(self):
        nestedList = [[1,1],2,[1,1]]
        itr = NestedIterator(nestedList)
        ans = []
        while itr.hasNext():
            ans.append(itr.next())
        self.assertEqual(ans, [1,1,2,1,1])

if __name__ == '__main__':
    unittest.main()

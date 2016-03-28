import unittest
from bidirectional_search import bidirectional_search


class Node:

    def __init__(self):
        self.adj = []


class TestBidirectionalSearch(unittest.TestCase):

    def setUp(self):
        n1 = Node()
        n2 = Node()
        n3 = Node()
        n4 = Node()
        n1.adj.append(n2)
        n2.adj.append(n1)
        n2.adj.append(n3)
        n3.adj.append(n2)
        n3.adj.append(n4)
        n4.adj.append(n3)
        self.s = n1
        self.t = n4

    def test(self):
        self.assertEqual(bidirectional_search(self.s, self.t), 3)

if __name__ == '__main__':
    unittest.main()

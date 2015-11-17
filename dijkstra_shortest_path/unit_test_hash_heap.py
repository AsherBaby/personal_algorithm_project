"""
HashHeap is also exhausted tested by Dijkstra extra large datasets.
"""
import unittest
from hash_heap import HashHeap
from dijkstra import DirectedGraphNode

class TestHashHeap(unittest.TestCase):

    def setUp(self):
        """
        Set up a hash heap with 5 nodes.
        First is id, second is the key used to compare in heap.
                1, 1
               /     \
             2, 5    3, 3
            /    \
          4, 7   5, 9
        """
        node1 = DirectedGraphNode(1, 1)
        node2 = DirectedGraphNode(2, 5)
        node3 = DirectedGraphNode(3, 3)
        node4 = DirectedGraphNode(4, 7)
        node5 = DirectedGraphNode(5, 9)
        nodes = [node1, node2, node3, node4, node5]
        hash_heap = HashHeap(key=lambda x: x.dist)
        for node in nodes:
            hash_heap.add(node)
        self.hash_heap = hash_heap

    def test_of_add(self):
        """
        Add node(6, 2)
        """
        hash_heap = self.hash_heap
        node6 = DirectedGraphNode(6, 2)
        hash_heap.add(node6)
        self.assertEqual(
            [node.id for node in hash_heap.heap],
            [1, 2, 6, 4, 5, 3])
        self.assertEqual(
            hash_heap.hash[node6], 2)

    def test_of_poll(self):
        self.assertEqual(
            self.hash_heap.poll().id, 1)

    def test_of_delete(self):
        """
        Add node(6, 2)
        Delete node(6, 2)
        """
        hash_heap = self.hash_heap
        node6 = DirectedGraphNode(6, 2)
        hash_heap.add(node6)
        hash_heap.delete(node6)
        self.assertEqual(
            [node.id for node in self.hash_heap.heap],
            [1, 2, 3, 4, 5])
        self.assertEqual(
            len(hash_heap.hash), 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)

import unittest
import connected_components_undirected_graph as cc

class TestWeakConnectedComponentsUndirectedGraph(unittest.TestCase):

    def setUp(self):
        """
        Set up the four nodes graph with node edges
        """
        node1 = cc.UndirectedGraphNode(1)
        node2 = cc.UndirectedGraphNode(2)
        node3 = cc.UndirectedGraphNode(3)
        node4 = cc.UndirectedGraphNode(4)
        self.nodes = [node1, node2, node3, node4]

    def test_of_four_components(self):
        """
        1 2 3 4
        """
        nodes = self.nodes
        self.assertEqual(
            cc.connected_components(nodes),
            [[1], [2], [3], [4]])

    def test_of_three_components(self):
        """
        1-2 3 4
        """
        nodes = self.nodes
        nodes[0].neighbors.append(nodes[1])
        nodes[1].neighbors.append(nodes[0])
        self.assertEqual(cc.connected_components(nodes), [[1, 2], [3], [4]])

    def test_of_two_components(self):
        """
        1-2-3 4
        """
        nodes = self.nodes
        nodes[0].neighbors.append(nodes[1])
        nodes[1].neighbors.append(nodes[0])
        nodes[1].neighbors.append(nodes[2])
        nodes[2].neighbors.append(nodes[1])
        self.assertEqual(cc.connected_components(nodes), [[1, 2, 3], [4]])

if __name__ == '__main__':
    unittest.main()

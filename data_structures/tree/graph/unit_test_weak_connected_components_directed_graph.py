import unittest
import weak_connected_components_directed_graph as wcc

class TestWeakConnectedComponentsDirectedGraph(unittest.TestCase):

    def setUp(self):
        """
        Set up the four nodes graph with node edges
        """
        node1 = wcc.DirectedGraphNode(1)
        node2 = wcc.DirectedGraphNode(2)
        node3 = wcc.DirectedGraphNode(3)
        node4 = wcc.DirectedGraphNode(4)
        self.nodes = [node1, node2, node3, node4]

    def test_of_four_components(self):
        """
        1 2 3 4
        """
        nodes = self.nodes
        self.assertEqual(
            wcc.weak_connected_components(nodes),
            [[1], [2], [3], [4]])

    def test_of_three_components(self):
        """
        1->2 3 4
        """
        nodes = self.nodes
        nodes[0].neighbors.append(nodes[1])
        self.assertEqual(wcc.weak_connected_components(nodes), [[1, 2], [3], [4]])

    def test_of_two_components(self):
        """
        1->2->3 4
        """
        nodes = self.nodes
        nodes[0].neighbors.append(nodes[1])
        nodes[1].neighbors.append(nodes[2])
        self.assertEqual(wcc.weak_connected_components(nodes), [[1, 2, 3], [4]])

    def test_of_one_components(self):
        """
        1->2->3<-4
        """
        nodes = self.nodes
        nodes[0].neighbors.append(nodes[1])
        nodes[1].neighbors.append(nodes[2])
        nodes[3].neighbors.append(nodes[2])
        self.assertEqual(wcc.weak_connected_components(nodes), [[1, 2, 3, 4]])

if __name__ == '__main__':
    unittest.main()

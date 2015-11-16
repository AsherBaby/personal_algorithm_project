import unittest
import strong_connected_components_directed_graph as sccdg

class TestStrongConnectedComponentsDirectedGraph(unittest.TestCase):

    def setUp(self):
        """
        Set up a four node graph
        1 -> 2 -> 4
        |         |
        . -> 3 -> .
        """
        node1 = sccdg.DirectedGraphNode(1)
        node2 = sccdg.DirectedGraphNode(2)
        node3 = sccdg.DirectedGraphNode(3)
        node4 = sccdg.DirectedGraphNode(4)
        graph = sccdg.Graph()
        graph[1] = node1
        graph[2] = node2
        graph[3] = node3
        graph[4] = node4
        graph[1].neighbors.append(graph[2])
        graph[2].neighbors.append(graph[4])
        graph[1].neighbors.append(graph[3])
        graph[3].neighbors.append(graph[4])
        self.graph = graph

    def test_graph_reverse(self):
        """
        After reverse:
        1 <- 2 <- 4
        |         |
        . <- 3 <- .
        """
        graph = self.graph
        graph = sccdg.graph_reverse(graph)
        self.assertEqual(len(graph[1].neighbors), 0)
        self.assertEqual([node.id for node in graph[2].neighbors], [1])
        self.assertEqual([node.id for node in graph[3].neighbors], [1])
        self.assertEqual(
            [node.id for node in graph[4].neighbors],
            [2, 3])

    def test_dfs_generate_seq(self):
        """
        1 -> 2 -> 4
        |         |
        . -> 3 -> .
        seq: [4, 2, 3, 1]
        """
        graph = self.graph
        self.assertEqual(sccdg.dfs_generate_seq(graph), [4,2,3,1])

    def test_scc_four_components(self):
        """
        1 -> 2 -> 4
        |         |
        . -> 3 -> .

        scc: [[4], [3], [2], [1]]
        """
        graph = self.graph
        graph[1].neighbors.append(graph[2])
        graph[2].neighbors.append(graph[4])
        graph[1].neighbors.append(graph[3])
        graph[3].neighbors.append(graph[4])
        self.assertEqual(sccdg.scc(graph), [[4], [3], [2], [1]])

    def test_scc_one_components(self):
        """
        . <- - <- .
        |         |
        1 -> 2 -> 4
        |         |
        . -> 3 -> .

        scc: [[1,2,4,3]
        """
        graph = self.graph
        graph[1].neighbors.append(graph[2])
        graph[2].neighbors.append(graph[4])
        graph[1].neighbors.append(graph[3])
        graph[3].neighbors.append(graph[4])
        graph[4].neighbors.append(graph[1])
        self.assertEqual(sccdg.scc(graph), [[1,2,4,3]])


if __name__ == '__main__':
    unittest.main(verbosity=2)

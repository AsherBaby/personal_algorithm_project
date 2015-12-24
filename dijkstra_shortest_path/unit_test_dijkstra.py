import unittest
from dijkstra import (
    dijkstra, DirectedGraphNode, DirectedGraphEdge, Graph)

class TestDijkstra(unittest.TestCase):

    def test_of_dijkstra_small_dataset(self):
        graph = Graph()
        graph.load('dijkstraDataSmall.txt')
        dijkstra(graph[1], graph)
        self.assertEqual(graph[4].dist, 2)

    def test_of_dijkstra_medium_dataset(self):
        graph = Graph()
        graph.load('dijkstraDataMedium.txt')
        dijkstra(graph[13], graph)
        self.assertEqual(graph[5].dist, 26)

    def test_of_dijkstra_large_dataset(self):
        graph = Graph()
        graph.load('dijkstraDataLarge.txt')
        dijkstra(graph[28], graph)
        self.assertEqual(graph[6].dist, 9)

    def test_of_dijkstra_extra_dataset(self):
        graph = Graph()
        graph.load('dijkstraDataExtra.txt')
        # Test data hornored verified by Coursera.org
        dijkstra(graph[1], graph)
        test_nodes_id = [7,37,59,82,99,115,133,165,188,197]
        distances = [graph[id].dist for id in test_nodes_id]
        self.assertEqual(
            distances,
            [2599,2610,2947,2052,2367,2399,2029,2442,2505,3068])


if __name__ == '__main__':
    unittest.main()

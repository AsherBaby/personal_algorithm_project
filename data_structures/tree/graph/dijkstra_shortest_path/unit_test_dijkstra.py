import unittest
from dijkstra import ShortestDist
from graph import Graph

class TestDijkstra(unittest.TestCase):

    def test_of_dijkstra_tiny_dataset(self):
        graph = Graph(filename='tinyG.txt')
        shortest_dist = ShortestDist(graph, 1)
        self.assertEqual(shortest_dist.dist(4), 2)

    def test_of_dijkstra_medium_dataset(self):
        graph = Graph(filename='mediumG.txt')
        shortest_dist = ShortestDist(graph, 13)
        self.assertEqual(shortest_dist.dist(5), 26)

    def test_of_dijkstra_large_dataset(self):
        graph = Graph(filename='largeG.txt')
        shortest_dist = ShortestDist(graph, 28)
        self.assertEqual(shortest_dist.dist(6), 9)

    def test_of_dijkstra_giant_dataset(self):
        graph = Graph(filename='giantG.txt')
        # Test data hornored verified by Coursera.org
        shortest_dist = ShortestDist(graph, 1)
        test_nodes_id = [7,37,59,82,99,115,133,165,188,197]
        distances = [shortest_dist.dist(id) for id in test_nodes_id]
        self.assertEqual(
            distances,
            [2599,2610,2947,2052,2367,2399,2029,2442,2505,3068])


if __name__ == '__main__':
    unittest.main()

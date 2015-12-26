"""
Directed graph data structure for Dijkstra algorithm
"""

class Node:

    def __init__(self, id):
        self.id = id
        self.edges = []
        self.dijkstra_dist = float('inf')

class Edge:

    def __init__(self, src, dest, dist):
        self.src = src
        self.dest = dest
        self.dist = dist

class Graph:

    def __init__(self, n=0, filename=None):
        """Adjacency list representation"""
        self.adj = [None] * n
        if filename:
            self._read_from_file(filename)

    def __getitem__(self, id):
        # get a node
        return self.adj[id]

    def __setitem__(self, id, val):
        # set a node
        self.adj[id] = val

    def __repr__(self):
        for node in self.adj:
            print(node.id, end=' ')
            for edge in node.edges:
                print(edge.dest, end=' ')
            print()

    def _read_from_file(self, filename):
        with open(filename) as fh:
            n = int(fh.readline().strip())
            self.adj = [None] * n  # a n nodes list
            adj = self.adj
            for line in fh:
                items = line.strip().split()
                id = int(items[0])
                adj[id] = Node(id)
                for pair in items[1:]:
                    adj_id, dist = pair.split(',')
                    adj_id = int(adj_id)
                    dist = int(dist)
                    edge = Edge(id, adj_id, dist)
                    adj[id].edges.append(edge)

"""Dijkstra's shortest path algorithm"""
from hash_heap import HashHeap

class DirectedGraphNode:

    def __init__(self, id, dist=float('inf')):
        self.id = id
        self.dist = dist
        self.edges = []

    def __hash__(self):
        return self.id

class DirectedGraphEdge:

    def __init__(self, dest, dist):
        self.dest = dest
        self.dist = dist

class Graph:
    """Graph class"""
    def __init__(self):
        """Adjacency list representation"""
        self.nodes = {}

    def __getitem__(self, id):
        return self.nodes[id]

    def __setitem__(self, id, val):
        self.nodes[id] = val

    def load(self, filename):
        nodes = self.nodes
        with open(filename) as fh:
            for line in fh:
                line = line.strip().split()
                id = int(line[0])
                nodes[id] = DirectedGraphNode(id)
                for pair in line[1:]:
                    pair = [int(each) for each in pair.split(',')]
                    edge = DirectedGraphEdge(*pair)
                    nodes[id].edges.append(edge)

def dijkstra(source, graph):
    """Dijkstra

    This method computes shortest distance and path for each node
    from the source node, and save results in each node's distance
    attribute.
    Return None
    """
    reachable = dfs(source, graph)
    for id in reachable:
        graph[id].dist = float('inf')
    source.dist = 0
    unknown = HashHeap(key=lambda node: node.dist)
    for node_id in reachable:
        unknown.add(graph[node_id])  # add to unknown
    visited = set()

    while len(unknown):
        node = unknown.poll()
        visited.add(node.id)  # add to known
        for edge in node.edges:
            neighbor = graph[edge.dest]
            if (edge.dest not in visited and
                    node.dist + edge.dist < neighbor.dist):
                neighbor.dist = node.dist + edge.dist
                unknown.update(neighbor)  # only in hash heap

def dfs(source, graph):
    """
    Return reachable nodes id as a list
    """
    visited = set()
    if source.id not in visited:
        visited.add(source.id)
        dfs_helper(source, graph, visited)
    return list(visited)

def dfs_helper(node, graph, visited):
    for edge in node.edges:
        if edge.dest not in visited:
            visited.add(edge.dest)
            dfs_helper(graph[edge.dest], graph, visited)

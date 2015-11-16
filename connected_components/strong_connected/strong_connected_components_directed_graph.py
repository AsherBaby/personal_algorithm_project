"""Strongly connected components for directed graph"""
from collections import deque

class DirectedGraphNode:

    def __init__(self, id):
        self.id = id
        self.neighbors = []

class Graph:

    def __init__(self):
        self.nodes = {}

    def __getitem__(self, id):
        return self.nodes[id]

    def __setitem__(self, id, value):
        self.nodes[id] = value

def scc(graph):
    reversed_graph = graph_reverse(graph)
    seq = dfs_generate_seq(reversed_graph)
    scc = dfs_compute_scc(graph, seq)
    return scc

def graph_reverse(graph):
    new_graph = Graph()
    for id in graph.nodes:
        new_graph[id] = DirectedGraphNode(id)
    for id, node in graph.nodes.items():
        for neighbor in node.neighbors:
            new_graph[neighbor.id].neighbors.append(new_graph[id])
    return new_graph

def dfs_generate_seq(graph):
    visited = set()
    seq = []
    for id, node in graph.nodes.items():
        if id not in visited:
            visited.add(id)
            dfs_generate_seq_helper(node, visited, seq)
    return seq

def dfs_generate_seq_helper(node, visited, seq):
    for neighbor in node.neighbors:
        if neighbor.id not in visited:
            visited.add(neighbor.id)
            dfs_generate_seq_helper(neighbor, visited, seq)
    seq.append(node.id)

def dfs_compute_scc(graph, seq):
    visited = set()
    scc = []
    for id in reversed(seq):
        node = graph[id]
        if id not in visited:
            visited.add(id)
            cluster = [id]
            dfs_compute_scc_helper(node, visited, cluster)
            scc.append(cluster)
    return scc

def dfs_compute_scc_helper(node, visited, cluster):
    for neighbor in node.neighbors:
        if neighbor.id not in visited:
            visited.add(neighbor.id)
            cluster.append(neighbor.id)
            dfs_compute_scc_helper(neighbor, visited, cluster)

"""Dijkstra's shortest path algorithm"""
from hash_heap import HashHeap
from graph import Graph
# import ipdb; ipdb.set_trace()


def dijkstra(graph, source):
    """Dijkstra

    This method computes shortest distance and path for each node
    from the source node, and save results in each node's distance
    attribute.
    return None
    """
    reachable = preprocessing(graph, source)
    for id in reachable:
        graph[id].dijkstra_dist = float('inf')
    source.dijkstra_dist = 0
    unknown = HashHeap(key=lambda x, y: x.dijkstra_dist < y.dijkstra_dist)
    for node_id in reachable:
        unknown.add(graph[node_id])  # add to unknown
    visited = set()

    while unknown:
        node = unknown.pop()
        visited.add(node.id)  # add to known
        for edge in node.edges:
            adj = graph[edge.dest]
            if (edge.dest not in visited and
                    node.dijkstra_dist + edge.dist < adj.dijkstra_dist):
                adj.dijkstra_dist = node.dijkstra_dist + edge.dist
                unknown.update(adj)  # method only in hash heap

def preprocessing(graph, source):
    """
    Return reachable nodes id as a list
    """
    marked = [False] * graph.n
    dfs(graph, source, marked)
    return [i for i, item in enumerate(marked) if item]

def dfs(graph, node, marked):
    marked[node.id] = True
    for edge in node.edges:
        adj = graph[edge.dest]
        if not marked[adj.id]:
            dfs(graph, adj, marked)

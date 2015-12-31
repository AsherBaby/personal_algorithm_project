"""Dijkstra's shortest path algorithm"""
from hash_heap import HashHeap
from graph import Graph


class ShortestDist:

    def __init__(self, graph, source_id):
        self.graph = graph
        self.source = graph[source_id]
        self.dists = [float('inf')] * len(graph)
        self.paths = [-1] * len(graph)
        self.dijkstra(self.graph, self.source)

    def dist(self, node_id):
        """ API: shortest distance from s to node_id """
        return self.dists[node_id]

    def path(self, node_id):
        """ API: shortest path from s to node_id (reversed) """
        if self.paths[node_id] == -1:
            return []
        stack = []
        while node_id != self.source.id:
            stack.append(node_id)
            node_id = self.paths[node_id]
        stack.append(self.source.id)
        return stack

    def dijkstra(self, graph, source):
        """Dijkstra

        This method computes shortest distance and path for each node
        from the source node, and save results in each node's distance
        attribute.
        return None
        """
        reachable = self.preprocessing(graph, source)
        self.dists[source.id] = 0
        self.paths[source.id] = source.id
        unknown = HashHeap(
            key=lambda x, y: self.dists[x.id] < self.dists[y.id])
        for node_id in reachable:
            unknown.add(graph[node_id])  # add to unknown
        marked = [False] * len(graph)

        while unknown:
            node = unknown.pop()
            marked[node.id] = True
            for edge in node.edges:
                adj = graph[edge.head]
                if (not marked[adj.id] and
                    self.dists[node.id] + edge.dist < self.dists[adj.id]):
                    self.dists[adj.id] = self.dists[node.id] + edge.dist
                    unknown.update(adj)  # method only in hash heap
                    self.paths[adj.id] = node.id

    def preprocessing(self, graph, source):
        """
        Return reachable nodes id as a list
        """
        marked = [False] * len(graph)
        self.dfs(graph, source, marked)
        return [i for i, item in enumerate(marked) if item]

    def dfs(self, graph, node, marked):
        marked[node.id] = True
        for edge in node.edges:
            adj = graph[edge.head]
            if not marked[adj.id]:
                self.dfs(graph, adj, marked)

from collections import deque

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

def connected_components(nodes):
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    if not nodes:
        return []

    visited = set()  # label
    queue = deque()
    result = []
    for start in nodes:
        if start.label not in visited:
            cluster = []
            visited.add(start.label)
            queue.append(start)
            while queue:
                node = queue.popleft()
                cluster.append(node.label)
                for neighbor in node.neighbors:
                    if neighbor.label not in visited:
                        visited.add(neighbor.label)
                        queue.append(neighbor)
            result.append(sorted(cluster))

    return result

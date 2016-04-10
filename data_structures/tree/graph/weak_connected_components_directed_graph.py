from union_find import UnionFind

class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


def weak_connected_components(nodes):
    # @param {DirectedGraphNode[]} nodes a array of directed graph node
    # @return {int[][]} a connected set of a directed graph
    union_find = UnionFind([node.label for node in nodes])
    for node in nodes:
        for neighbor in node.neighbors:
            union_find.union(node.label, neighbor.label)

    return transform_to_cluster(union_find)

def transform_to_cluster(union_find):
    hash_cluster = {}
    for node in union_find.father:
        father = union_find.find(node)
        if father not in hash_cluster:
            hash_cluster[father] = [node]
        else:
            hash_cluster[father].append(node)

    list_cluster = []
    for father, cluster in hash_cluster.items():
        list_cluster.append(sorted(cluster))

    return list_cluster

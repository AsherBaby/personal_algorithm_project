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

    return union_find.transform_to_cluster()


class UnionFind:

    def __init__(self, ids):
        self.disjoint_set = {}
        for id in ids:
            self.disjoint_set[id] = id

    def union(self, a, b):
        # a => b
        father_a = self.find(a)
        father_b = self.find(b)
        self.disjoint_set[father_a] = father_b

    def find(self, a):
        father = self.disjoint_set[a]
        while father != self.disjoint_set[father]:
            father = self.disjoint_set[father]
        return father

    def transform_to_cluster(self):
        hash_cluster = {}
        for node in self.disjoint_set:
            father = self.find(node)
            if father not in hash_cluster:
                hash_cluster[father] = [node]
            else:
                hash_cluster[father].append(node)

        list_cluster = []
        for father, cluster in hash_cluster.items():
            list_cluster.append(sorted(cluster))

        return list_cluster

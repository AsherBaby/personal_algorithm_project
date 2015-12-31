class UnionFind:

    def __init__(self, ids):
        self.father = {}
        for id in ids:
            self.father[id] = id

    def union(self, a, b):
        """Combine root of a with root of b"""
        root_a = self.find(a)
        root_b = self.find(b)
        self.father[root_a] = root_b

    def find(self, a):
        """Find root of a"""
        root = self.father[a]
        while root != self.father[root]:
            root = self.father[root]
        while a != root:  # path compression
            tmp = self.father[a]
            self.father[a] = root
            a= tmp
        return root

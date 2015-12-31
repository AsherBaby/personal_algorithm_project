
class Node:

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.name

class SymbolGraph:

    def __init__(self):
        self.adj = set()

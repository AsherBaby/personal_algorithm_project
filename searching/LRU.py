"""
LRU: least recently used cache algorithm

Implementation:
    Dummy + Double linked list + Hash
"""

class LRUCache:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, n):
        self.capacity = n
        self.dummy = LRUCache.Node(0, 0)
        self.tail = self.dummy
        self.hash = dict()

    def get(self, key):
        if key not in self.hash:
            return
        node = self.hash[key]
        if node != self.tail:
            self.pop(node)
            self.append(node)
        return node.value

    def set(self, key, value):
        if key in self.hash:
            node = self.hash[key]
            if node != self.tail:
                self.pop(node)
                self.append(node)
            node.value = value
        else:
            if len(self.hash) < self.capacity:
                node = LRUCache.Node(key, value)
                self.hash[key] = node
                self.append(node)
            else:
                self.modify(self.dummy.next.key, key, value)
                node = self.hash[key]
                if node != self.tail:
                    self.pop(node)
                    self.append(node)

    def pop(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def append(self, node):
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        node.next = None

    def modify(self, old_key, key, value):
        node = self.hash[old_key]
        del self.hash[old_key]
        self.hash[key] = node
        node.key = key
        node.value = value

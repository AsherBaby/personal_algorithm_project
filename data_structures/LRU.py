"""
LRU: least recently used cache algorithm
"""
from linked_hash_map import LinkedHashMap


class LRUCache:

    def __init__(self, cap):
        self.cache = LinkedHashMap(cap)

    def get(self, key):
        if key not in self.cache.ht:
            return
        self._move_to_head(key)
        return self.cache.ht[key].value

    def set(self, key, value):
        if key in self.cache.ht:
            self.cache.ht[key].value = value
            self._move_to_head(key)
        else:
            if not self.cache.full():
                self.cache.insert(key, value)
            else:
                del self.cache.ht[self.cache.dummy_tail.left.key]
                self.cache.ht[key] = self.cache.dummy_tail.left
                self.cache.ht[key].key = key
                self.cache.ht[key].value = value
                self._move_to_head(key)

    def _move_to_head(self, key):
        node = self.cache.ht[key]
        node.left.right = node.right
        node.right.left = node.left
        node.right = self.cache.dummy_head.right
        node.left = self.cache.dummy_head
        self.cache.dummy_head.right = node
        node.right.left = node

"""
LRU: least recently used cache algorithm
"""
from linked_hash_map import LinkedHashMap


class LRUCache:

    def __init__(self, cap):
        self.cache = LinkedHashMap(cap)

    def get(self, key):
        ans = self.cache.get(key)  # get()
        if ans is None:
            return
        self._move_to_head(key)
        return ans

    def set(self, key, value):
        if key in self.cache:
            self.cache[key].value = value
            self._move_to_head(key)
        else:
            if self.cache.full():  # full()
                self._remove_last()
            self.cache.insert(key, value)  # insert()

    def _move_to_head(self, key):
        value = self.cache[key].value
        self.cache.remove(key)  # remove()
        self.cache.insert(key, value)  # insert()

    def _remove_last(self):
        self.cache.remove(self.cache.dummy_tail.left.key)  # remove()

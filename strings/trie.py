"""
A trie implementation that powerfully supports prefix searching.

Trie or R-trie is sweet for small strings and small alphabet.
The performance of trie is hard to beat if you can afford the space :)
"""

class Trie:
    class Node:
        def __init__(self, R):
            self.next = [None] * R
            self.val = None

    def __init__(self, R):
        self.R = R
        self.root = self.Node(R)

    def _idx(self, c):
        return ord(c) - ord('a')

    def get(self, key):
        # return value if key exists
        node = self.root
        for c in key:
            node = node.next[self._idx(c)]
            if not node:
                return
        return node.val

    def insert(self, key, val):
        node = self.root
        for c in key:
            if not node.next[self._idx(c)]:
                node.next[self._idx(c)] = self.Node(self.R)
            node = node.next[self._idx(c)]
        node.val = val

    def keys_with_prefix(self, prefix):
        node = self.root
        for c in prefix:
            node = node.next[self._idx(c)]
            if not node:
                return
        keys = []
        key = list(prefix)
        self._dfs(node, key, keys)
        return keys

    def num_keys_with_prefix(self, prefix):
        node = self.root
        for c in prefix:
            node = node.next[self._idx(c)]
            if not node:
                return
        count = [0]
        key = list(prefix)
        self._dfs2(node, key, count)
        return count[0]

    def _dfs(self, node, key, keys):
        if not node:
            return
        if node.val is not None:
            keys.append(''.join(key))
        for i in range(self.R):
            key.append(self._chr(i))
            self._dfs(node.next[i], key, keys)
            key.pop()

    def _dfs2(self, node, key, count):
        if not node:
            return
        if node.val is not None:
            count[0] += 1
        for i in range(self.R):
            key.append(self._chr(i))
            self._dfs2(node.next[i], key, count)
            key.pop()

    def _chr(self, i):
        return chr(i+ord('a'))

"""
A trie implementation that powerfully supports prefix searching.

Trie or R-trie is sweet for small strings and small alphabet.
The performance of trie is hard to beat if you can afford the space :)
"""

class Trie:
    class Node:
        def __init__(self, R):
            self.val = None
            self.next = [None] * R

    def __init__(self, R):
        self.root = self.Node(R)
        self.R = R

    def get(self, key):
        node = self.root
        for c in key:
            node = node.next[ord(c)-ord('a')]
            if not node:
                return
        return node.val

    def insert(self, key, val):
        node = self.root
        for c in key:
            if not node.next[ord(c)-ord('a')]:
                node.next[ord(c)-ord('a')] = self.Node(self.R)
            node = node.next[ord(c)-ord('a')]
        node.val = val

    def keys_with_prefix(self, prefix):
        node = self.root
        for c in prefix:
            node = node.next[ord(c)-ord('a')]
            if not node:
                return
        self.keys = []
        self.dfs(node, prefix)
        return self.keys

    def dfs(self, node, key):
        if not node:
            return
        if node.val is not None:  #
            self.keys.append(key)
        for i in range(self.R):
            self.dfs(node.next[i], key+chr(i+ord('a')))

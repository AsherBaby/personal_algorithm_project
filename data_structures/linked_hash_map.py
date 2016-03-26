"""
Linked Hash Map data structure, especially useful for LRU cache.
It can quickly locate an element, and put it to the end of linked list.
"""
import math


class LinkedHashMap:


    class ListNode:

        def __init__(self, key, value):
            self.left = None
            self.right = None
            self.key = key
            self.value = value

    def __init__(self, cap=math.inf):
        self.dummy_head = self.ListNode(0, 0)
        self.dummy_tail = self.ListNode(0, 0)
        self.dummy_head.right = self.dummy_tail
        self.dummy_tail.left = self.dummy_head
        self.ht = {}
        self.cap = cap

    def full(self):
        return len(self.ht) >= self.cap

    def insert(self, key, value):
        # insert at beginning
        node = self.ListNode(key, value)
        self.ht[key] = node
        node.left = self.dummy_head
        node.right = self.dummy_head.right
        self.dummy_head.right = node
        node.right.left = node

    def get(self, key):
        if key not in self.ht:
            return
        return self.ht[key].value

    def remove(self, key):
        node = self.ht[key]
        node.left.right = node.right
        node.right.left = node.left
        del self.ht[key]

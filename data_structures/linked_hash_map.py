"""
Linked Hash Map data structure, especially useful for LRU cache.
It can quickly locate an element, and put it to the end of linked list.
"""
import math


class LinkedHashMap:


    class ListNode:

        def __init__(self, value):
            self.prev = None
            self.next = None
            self.value = value

    def __init__(self, cap=math.inf):
        self.dummy = self.ListNode(0)
        self.tail = self.dummy
        self.ht = {}
        self.size = 0
        self.cap = cap

    def insert(self, key, value):
        node = self.ListNode(value)
        self.ht[key] = node
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def get(self, key):
        if key not in self.ht:
            return
        return self.ht[key].value

    def remove(self, key):
        node = self.ht[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.ht[key]

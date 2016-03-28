"""

Bidirectional search, basically bfs from source and target both, until hit.
Bidirectional search only works for undirected graph.
"""
from collections import deque


def bidirectional_search(s, t):
    queue_s = deque([s])
    queue_t = deque([t])
    seen_s = set([s])
    seen_t = set([t])
    flag = True
    d = 0
    while queue_s and queue_t:
        d += 1
        if flag:
            if bfs(queue_s, seen_s, seen_t):
                return d
        else:
            if bfs(queue_t, seen_t, seen_s):
                return d
        flag = not flag
    return -1

def bfs(queue, seen, seen_other):
    size = len(queue)
    for i in range(size):
        node = queue.popleft()
        for adj in node.adj:
            if adj in seen_other:
                return True
            if adj not in seen:
                seen.add(adj)
                queue.append(adj)

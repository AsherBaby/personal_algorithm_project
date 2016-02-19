from hash_heap import HashHeap

class Point:
    def __init__(self, x, height, is_start):
        self.x = x
        self.height = height
        self.is_start = is_start

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        else:
            if self.is_start and other.is_start:
                # add higher start first
                return self.height > other.height
            elif not self.is_start and not other.is_start:
                # remove lower end first
                return self.height < other.height
            else:
                # start < end
                return self.is_start

def building_outlines(buildings):
    points = []
    for b in buildings:
        start, end, height = b[0], b[1], b[2]
        points.append(Point(start, height, True))
        points.append(Point(end, height, False))
    points.sort()
    ans = []
    heap = HashHeap('max')
    start = 0
    for p in points:
        if p.is_start:
            if not heap or heap.top() < p.height:
                if heap:
                    ans.append([start, p.x, heap.top()])
                start = p.x
            heap.add(p.height)
        else:
            height = heap.top()
            heap.delete(p.height)
            if not heap or heap.top() < height:
                ans.append([start, p.x, height])
                start = p.x
    return ans

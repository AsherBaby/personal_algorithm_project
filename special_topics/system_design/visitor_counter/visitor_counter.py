"""
Count how many visitors has come to store in an hour with precision to a minute.
"""
from collections import deque
from threading import Lock

class VisitorCounterByQueue:

    class Hit:
        def __init__(self, time):
            self.time = time
            self.cnt = 1

    def __init__(self):
        self.queue = deque(maxlen=60)

    def log_hit(self, time):
        if self.queue and time == self.queue[-1].time:
            self.queue[-1].cnt += 1
        else:
            if len(self.queue) == self.queue.maxlen:
                queue.popleft()
            self.queue.append(self.Hit(time))

    def get_hit(self, time):
        while self.queue and time - self.queue[0].time >= 60:
            self.queue.popleft()
        ans = 0
        for hit in self.queue:
            ans += hit.cnt
        return ans

class VisitorCounterByArray:
    """
    time bucket
    """

    def __init__(self):
        self.time_array = list(range(60))
        self.cnt_array = [0] * 60
        self.lock = Lock()

    def log_hit(self, time):
        # write
        idx = time % 60
        with self.lock:
            if time - self.time_array[idx] >= 60:
                self.time_array[idx] = time
                self.cnt_array[idx] = 1
            else:
                self.cnt_array[idx] += 1

    def get_hit(self, time):
        # read
        cnt = 0
        for i in range(60):
            with self.lock:
                if time - self.time_array[i] < 60:
                    cnt += self.cnt_array[i]
        return cnt

from collections import deque
from threading import Thread, Semaphore, Lock

class Queue:
    '''A thread-safe task list implemented with semaphore.'''

    def __init__(self):
        self.lock = Lock()
        self.semaphore = Semaphore(value=0)
        self.data = deque()

    def push(self, x):
        with self.lock:
            self.semaphore.release()
            self.data.append(x)

    def pop(self):
        self.semaphore.acquire()
        with self.lock:
            self.data.popleft()

from collections import deque
from threading import Condition as CV

class Queue:
    '''A thread-safe queue implemented with condition variable.'''

    def __init__(self):
        self.cv = CV()
        self.data = deque()

    def push(self, x):
        with self.cv:
            self.data.append(x)
            self.cv.notify()

    def pop(self):
        with self.cv:
            while not self.data:
                self.cv.wait()
            self.data.popleft()

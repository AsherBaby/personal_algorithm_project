from threading import Thread, Semaphore, Lock
from random import shuffle

class TaskList:
    '''A thread-safe task list implemented with semaphore.'''

    def __init__(self):
        self.n = 0
        self.lock = Lock()
        self.semaphore = Semaphore(value=0)
        self.dummy_list = []

    def has_task(self):
        return self.n > 0

    def add_task(self, a):
        semaphore = self.semaphore
        lock = self.lock
        with lock:
            self.n += a
            self.dummy_list.append(self.n)
            for i in range(a):
                semaphore.release()

    def get_task(self):
        semaphore = self.semaphore
        lock = self.lock
        semaphore.acquire()
        with lock:
            self.n -= 1
            self.dummy_list.append(self.n)

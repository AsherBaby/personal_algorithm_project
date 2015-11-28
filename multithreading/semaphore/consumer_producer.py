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
        lock.acquire()
        self.n += a
        self.dummy_list.append(self.n)
        for i in range(a):
            semaphore.release()
        lock.release()

    def get_task(self):
        semaphore = self.semaphore
        lock = self.lock
        semaphore.acquire()
        lock.acquire()
        self.n -= 1
        self.dummy_list.append(self.n)
        lock.release()

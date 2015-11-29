from threading import Condition

class TaskList:
    '''A thread-safe task list implemented with condition variable.'''

    def __init__(self):
        self.n = 0
        self.cv = Condition()
        self.dummy_list = []

    def has_task(self):
        return self.n > 0

    def add_task(self, a):
        cv = self.cv
        with cv:
            self.n += a
            cv.notify(n=a)
            self.dummy_list.append(self.n)

    def get_task(self):
        cv = self.cv
        with cv:
            while not self.has_task():
                cv.wait()
            self.n -= 1
            self.dummy_list.append(self.n)

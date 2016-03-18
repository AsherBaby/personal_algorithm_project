import unittest
from threading import Thread
from condition_variable import Queue

class TestTaskList(unittest.TestCase):

    def test_thread_safe(self):
        tasks = Queue()  # shared object
        t1 = Thread(target=tasks.pop)
        t2 = Thread(target=tasks.pop)
        t3 = Thread(target=tasks.push, args=(4,))
        t4 = Thread(target=tasks.push, args=(2,))
        threads = [t1, t2, t3, t4]
        for t in threads:
            t.start()  # pop will wait push first
        for t in threads:
            t.join()

if __name__ == '__main__':
    unittest.main()

import unittest
from threading import Thread
from random import shuffle
from consumer_producer import TaskList

class TestTaskList(unittest.TestCase):

    def test_thread_safe(self):
        tasks = TaskList()  # shared object
        t1 = Thread(target=tasks.add_task, args=(4,))
        t2 = Thread(target=tasks.get_task)
        t3 = Thread(target=tasks.get_task)
        t4 = Thread(target=tasks.get_task)
        t5 = Thread(target=tasks.get_task)
        threads = [t1, t2, t3, t4, t5]
        shuffle(threads)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(
            tasks.dummy_list, [4,3,2,1,0])

if __name__ == '__main__':
    unittest.main()

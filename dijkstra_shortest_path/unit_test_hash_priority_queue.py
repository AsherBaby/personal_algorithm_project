import unittest
from hash_priority_queue import HashPriorityQueue

class TestHashPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = HashPriorityQueue()
        array = [8, 5, 3, 9, 6, 4, 2, 6]
        for n in array:
            self.pq.add(n)

    # def tearDown(self)

    def test_of_add(self):
        for i in range(1, len(self.pq.heap)):
            p = (i - 1) // 2
            self.assertLess(
                self.pq.heap[p], self.pq.heap[i])

    def test_of_pop(self):
        sorted_array = []
        while self.pq:
            sorted_array.append(self.pq.pop())
        for i in range(1, len(sorted_array)):
            self.assertLessEqual(
                sorted_array[i-1], sorted_array[i])

    def test_of_delete(self):
        self.pq.delete(5)
        self.pq.delete(6)
        self.pq.delete(-1)
        for i in range(1, len(self.pq.heap)):
            p = (i - 1) // 2
            self.assertLess(
                self.pq.heap[p], self.pq.heap[i])
        self.assertFalse(5 in self.pq)
        self.assertTrue(6 in self.pq)


if __name__ == '__main__':
    unittest.main()

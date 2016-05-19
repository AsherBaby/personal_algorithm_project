"""
Quick sort using divide and conquer
"""
import random


class QuickSort:

    @staticmethod
    def sort(array):
        if len(array) == 0:
            return array
        QuickSort.sortHelper(array, 0, len(array)-1)

    @staticmethod
    def sortHelper(array, l, r):
        if l >= r:
            return

        pivot = QuickSort.partition(array, l, r)
        QuickSort.sortHelper(array, l, pivot-1)
        QuickSort.sortHelper(array, pivot+1, r)

    @staticmethod
    def partition(array, l, r):
        pivot = random.randint(l, r)

        array[l], array[pivot] = array[pivot], array[l]
        x = array[l]

        smaller = l+1
        for walk in range(l+1, r+1):
            if array[walk] < x:
                array[smaller], array[walk] = array[walk], array[smaller]
                smaller += 1

        smaller -= 1
        array[smaller], array[l] = array[l], array[smaller]

        return smaller


array = random.sample(range(1000), 1)
QuickSort.sort(array)
print(array)

array = random.sample(range(1000), 2)
QuickSort.sort(array)
print(array)

array = random.sample(range(1000), 20)
QuickSort.sort(array)
print(array)

import unittest
import random

from practice.y2016.basic import solve_skyline as solve_skyline

from practice.y2016.basic import heap_sort as do_sort
from practice.y2016.basic import PriorityQueue as PriorityQueue

from practice.y2016.basic import binary_search as binary_search
from practice.y2016.basic import atoi as atoi
from practice.y2016.basic import reverse_words


class TestSorting(unittest.TestCase):

    def test_sort(self):
        # import sorting function as do_sort
        for i in xrange(1, 20):
            # Do it 5 times
            expected = range(i)
            for i in xrange(5):
                mlist = expected[:]
                random.shuffle(mlist)
                # print mlist
                self.assertEqual(do_sort(mlist), expected)

        pass


class TestBasic(unittest.TestCase):

    def test_reverse_words(self):
        self.assertEqual(reverse_words("Hello World"), "World Hello")
        self.assertEqual(reverse_words("I Love You"), "You Love I")

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 2, 3], 4), -1)
        self.assertEqual(binary_search([1, 2, 3], 3), 2)
        self.assertEqual(binary_search([1, 2, 3], 2), 1)
        self.assertEqual(binary_search([1, 2, 3], 1), 0)

        self.assertEqual(binary_search([], 2), -1)
        self.assertEqual(binary_search([1], 2), -1)
        self.assertEqual(binary_search([1], -2), -1)

        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 2), 1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_atoi(self):
        self.assertEqual(atoi("123"), int("123"))
        self.assertEqual(atoi("-123"), int("-123"))
        self.assertEqual(atoi("0"), int("0"))
        self.assertEqual(atoi("-0"), int("-0"))


class TestSkyline(unittest.TestCase):

    def test_inout(self):
        buildings = [(2, 9, 10), (3, 6, 15), (5, 12, 12), (13, 16, 10), (13, 16, 10), (15, 17, 5)]
        skyline = [(2, 10), (3, 15), (6, 12), (12, 0), (13, 10), (16, 5), (17, 0)]
        self.assertEqual(solve_skyline(buildings), skyline)

        buildings = [(2, 9, 10), (3, 7, 15), (5, 12, 12), (15, 20, 10), (19, 24, 8)]
        skyline = [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10), (20, 8), (24, 0)]
        self.assertEqual(solve_skyline(buildings), skyline)

        buildings = [(1,11,5), (2,6,7), (3,13,9), (12,7,16), (14,3,25), (19,18,22), (23,13,29), (24,4,28)]
        skyline = [(1, 11), (3, 13), (9, 0), (12, 7), (16, 3), (19, 18), (22, 3), (25, 0)]
        self.assertEqual(solve_skyline(buildings), skyline)

        buildings = [(1, 5, 11), (2, 7, 6), (3, 9, 13), (12, 16, 7), (14, 25, 3), (19, 22, 18), (23, 29, 13), (24, 28, 4)]
        skyline = [(1, 11), (3, 13), (9, 0), (12, 7), (16, 3), (19, 18), (22, 3), (23, 13), (29, 0)]
        self.assertEqual(solve_skyline(buildings), skyline)

        pass

    def test_corner_cases(self):
        # One building completely overlap on the other
        buildings = [(2, 5, 5), (2, 5, 9)]
        skyline = [(2, 9), (5, 0)]
        self.assertEqual(solve_skyline(buildings), skyline)


class TestPriorityQueue(unittest.TestCase):

    def test_output(self):

        queue = PriorityQueue()
        queue.add_task("Write code", 5)
        queue.add_task("Write spec", 7)
        queue.add_task("Create tests", 3)
        queue.add_task("Write user docs", 1)

        print queue

        task = queue.pop_task()
        self.assertEqual(task, "Write spec")

        # Update priority of "Create tests"
        queue.add_task("Create tests", 6)
        print queue
        task = queue.pop_task()
        self.assertEqual(task, "Create tests")

        # Remove task "Write user docs"
        queue.remove_task("Write user docs")
        print queue

        task = queue.pop_task()
        self.assertEqual(task, "Write code")
        print queue


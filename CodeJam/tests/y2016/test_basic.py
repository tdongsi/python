
from __future__ import absolute_import

import unittest
import random

import practice.y2016.basic as basic
from practice.y2016.basic import solve_skyline as solve_skyline

from practice.y2016.basic import quicksort3 as do_sort
from practice.y2016.basic import PriorityQueue as PriorityQueue

from practice.y2016.basic import binary_search as binary_search
from practice.y2016.basic import atoi as atoi
from practice.y2016.basic import reverse_words
from practice.y2016.basic import spiral_list


class TestSearch(unittest.TestCase):

    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}

    def test_dfs(self):
        search = basic.dfs(self.graph, 'A')
        self.assertEqual(search, ['A', 'B', 'D', 'E', 'F', 'C'])
        pass

    def test_bfs(self):
        search = basic.bfs(self.graph, 'A')
        self.assertEqual(search, ['A', 'C', 'B', 'F', 'E', 'D'])
        pass


class TestSpiralPrint(unittest.TestCase):

    def test_corner(self):
        input = [[1]]
        self.assertEqual(spiral_list(input), [1])

        input = [[1], [2]]
        self.assertEqual(spiral_list(input), [1, 2])

    def test_case1(self):
        # Expected is a list from 1-25, inclusive
        expected = range(26)
        del expected[0]

        input = [[1, 2, 3, 4, 5],
                 [16, 17, 18, 19, 6],
                 [15, 24, 25, 20, 7],
                 [14, 23, 22, 21, 8],
                 [13, 12, 11, 10, 9]]

        self.assertEqual(spiral_list(input), expected)

        pass


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

    def test_same_element(self):

        self.assertEqual(do_sort([2, 3, 5, 7, 4, 2, 6, 1]), [1, 2, 2, 3, 4, 5, 6, 7])
        self.assertEqual(do_sort([2, 2]), [2, 2])
        self.assertEqual(do_sort([1, 2, 1]), [1, 1, 2])
        self.assertEqual(do_sort([2, 3, 1, 2, 2, 4, 3, 1]), [1, 1, 2, 2, 2, 3, 3, 4])
        self.assertEqual(do_sort([2, 1]), [1, 2])
        pass


class TestBasic(unittest.TestCase):

    def test_median(self):
        self.assertEqual(basic.find_median([1, 5, 2]), 2)
        self.assertEqual(basic.find_median([-5, -1, -3]), -3)
        self.assertEqual(basic.find_median([8, 2, 7,  6]), 6.5)

        self.assertEqual(basic.find_median([3]), 3)
        self.assertEqual(basic.find_median([]), None)
        pass

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

    def check(self, first, second, out):
        out_shape = [basic.Point(e[0], e[1]) for e in out]
        shape1 = [basic.Point(e[0], e[1]) for e in first]
        shape2 = [basic.Point(e[0], e[1]) for e in second]
        self.assertEqual(out_shape, basic.merge_skyline(shape1, shape2))
        return out_shape

    def test_debug(self):
        first = [(1, 4), (3, 6), (9, 5), (11, 0)]
        second = [(2, 3), (6, 8), (8, 4), (10, 7), (12, 0)]
        out = [(1, 4), (3, 6), (6, 8), (8, 6), (9, 5), (10, 7), (12, 0)]
        self.check(first, second, out)

    def test_overlap(self):
        first = [(1, 4), (3, 6), (9, 5), (11, 0)]
        second = [(2, 3), (6, 8), (8, 4), (10, 7), (12, 0)]
        out = [(1, 4), (3, 6), (6, 8), (8, 6), (9, 5), (10, 7), (12, 0)]
        self.check(first, second, out)
        self.check(second, first, out)

        # non-overlapping
        first = [(1, 4), (3, 6), (9, 0)]
        second = [(10, 7), (12, 0)]
        out = [(1, 4), (3, 6), (9, 0), (10, 7), (12, 0)]
        self.check(first, second, out)
        self.check(second, first, out)

        pass

    def test_inout(self):
        buildings = [(2, 9, 10), (3, 6, 15), (5, 12, 12), (13, 16, 10), (13, 16, 10), (15, 17, 5)]
        skyline = [(2, 10), (3, 15), (6, 12), (12, 0), (13, 10), (16, 5), (17, 0)]
        self.assertEqual(solve_skyline(buildings), skyline)

        buildings = [(2, 9, 10), (3, 7, 15), (5, 12, 12), (15, 20, 10), (19, 24, 8)]
        skyline = [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10), (20, 8), (24, 0)]
        self.assertEqual(solve_skyline(buildings), skyline)

        buildings_wrong = [(1,11,5), (2,6,7), (3,13,9), (12,7,16), (14,3,25), (19,18,22), (23,13,29), (24,4,28)]
        buildings = [(building[0], building[2], building[1]) for building in buildings_wrong]
        skyline = [(1, 11), (3, 13), (9, 0), (12, 7), (16, 3), (19, 18), (22, 3), (23, 13), (29, 0)]
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
        queue.add("Write code", 5)
        self.assertEqual((5, "Write code"), queue.peek())
        queue.add("Write spec", 7)
        self.assertEqual((7, "Write spec"), queue.peek())
        queue.add("Create tests", 3)
        self.assertEqual((7, "Write spec"), queue.peek())
        queue.add("Write user docs", 1)
        self.assertEqual((7, "Write spec"), queue.peek())

        print queue

        task = queue.pop()
        self.assertEqual(task[1], "Write spec")
        self.assertEqual((5, "Write code"), queue.peek())

        # Update priority of "Create tests"
        queue.add("Create tests", 6)
        self.assertEqual((6, "Create tests"), queue.peek())
        task = queue.pop()
        self.assertEqual(task[1], "Create tests")

        # Remove task "Write user docs"
        queue.remove("Write user docs")
        self.assertEqual((5, "Write code"), queue.peek())

        task = queue.pop()
        self.assertEqual(task[1], "Write code")
        self.assertEqual(None, queue.peek())



import unittest
import random

from practice.y2016.basic import heap_sort as do_sort
from practice.y2016.basic import bin_search as binary_search
from practice.y2016.basic import atoi as atoi


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


import unittest

import practice.y2016.basic as bs


class TestBinarySearch(unittest.TestCase):

    def test_functional(self):
        self.assertEqual(bs.bin_search([1, 2, 3], 4), -1)
        self.assertEqual(bs.bin_search([1, 2, 3], 3), 2)
        self.assertEqual(bs.bin_search([1, 2, 3], 2), 1)
        self.assertEqual(bs.bin_search([1, 2, 3], 1), 0)

        self.assertEqual(bs.bin_search([], 2), -1)
        self.assertEqual(bs.bin_search([1], 2), -1)
        self.assertEqual(bs.bin_search([1], -2), -1)

        self.assertEqual(bs.bin_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(bs.bin_search([1, 2, 3, 4, 5], 2), 1)
        self.assertEqual(bs.bin_search([1, 2, 3, 4, 5], 1), 0)

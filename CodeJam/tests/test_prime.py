
import unittest

import codejam.prime as pr

class PseudoPrimeTest(unittest.TestCase):

    def test_is_pseudo_prime(self):

        self.assertFalse(pr.is_pseudo_prime(561))
        self.assertFalse(pr.is_pseudo_prime(703))
        self.assertTrue(pr.is_pseudo_prime(701))
        self.assertTrue(pr.is_pseudo_prime(977))

        self.assertFalse(pr.is_pseudo_prime(443*991))
        self.assertFalse(pr.is_pseudo_prime(601*811))

    def test_find_factor(self):

        self.assertTrue(pr.find_factor(561) > 1)
        self.assertTrue(pr.find_factor(703) > 1)
        self.assertEqual(pr.find_factor(701), 1)
        self.assertEqual(pr.find_factor(977), 1)

        self.assertTrue(pr.find_factor(341) > 1)

        self.assertTrue(pr.find_factor(443*991) > 1)
        # self.assertEqual(pr.find_factor(601*811, 50), 601)
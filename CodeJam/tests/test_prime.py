
import unittest

import codejam.prime as pr

class PseudoPrimeTest(unittest.TestCase):

    def test_is_pseudo_prime(self):

        self.assertFalse(pr.is_pseudo_prime(561))
        self.assertFalse(pr.is_pseudo_prime(703))
        self.assertTrue(pr.is_pseudo_prime(701))
        self.assertTrue(pr.is_pseudo_prime(977))

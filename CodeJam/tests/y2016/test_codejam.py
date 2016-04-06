
import unittest
import StringIO

from practice.y2016.codejam import StoreCredit

PROJECT_HOME = "/Users/cdongsi/Hub/python/CodeJam"


class StoreCreditTest(unittest.TestCase):

    def test_example(self):
        solver = StoreCredit(PROJECT_HOME + "/data/StoreCredit.txt")
        str_output = StringIO.StringIO()

        solver.solve(output=str_output)
        actual = str_output.getvalue()
        expected = ("Case #1: 2 3\n"
                    "Case #2: 1 4\n"
                    "Case #3: 4 5\n")
        self.assertEqual(actual, expected)

        str_output.close()
        pass

    def test_small_input(self):
        solver = StoreCredit(PROJECT_HOME + "/data/A-small-practice.in")
        with open("out.txt", "w") as f:
            solver.solve(output=f)
        pass

    def test_large_input(self):
        solver = StoreCredit(PROJECT_HOME + "/data/A-large-practice.in")
        with open("out.txt", "w") as f:
            solver.solve(output=f)
        pass

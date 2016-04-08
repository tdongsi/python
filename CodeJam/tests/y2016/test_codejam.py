
import unittest
import StringIO

import practice.y2016.codejam as cj

PROJECT_HOME = "/Users/cdongsi/Hub/python/CodeJam"


class StoreCreditTest(unittest.TestCase):

    def test_example(self):
        solver = cj.StoreCredit(PROJECT_HOME + "/data/StoreCredit.txt")
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
        solver = cj.StoreCredit(PROJECT_HOME + "/data/A-small-practice.in")
        with open("out.txt", "w") as f:
            solver.solve(output=f)
        pass

    def test_large_input(self):
        solver = cj.StoreCredit(PROJECT_HOME + "/data/A-large-practice.in")
        with open("out.txt", "w") as f:
            solver.solve(output=f)
        pass


class ReverseWordsTest(unittest.TestCase):

    def test_small_input(self):
        solver = cj.ReverseWords(PROJECT_HOME + "/data/B-small-practice.in")
        with open("out.txt", "w") as f:
            solver.solve(output=f)
        pass

    def test_large_input(self):
        solver = cj.ReverseWords(PROJECT_HOME + "/data/B-large-practice.in")
        with open("out.txt", "w") as f:
            solver.solve(output=f)
        pass


class AlienLanguageTest(unittest.TestCase):

    def test_example(self):
        solver = cj.AlienLanguage(PROJECT_HOME + "/data/AlienLanguage.txt")
        str_output = StringIO.StringIO()
        solver.solve(output=str_output)
        actual = str_output.getvalue()
        expected = ("Case #1: 2\n"
                    "Case #2: 1\n"
                    "Case #3: 3\n"
                    "Case #4: 0\n")
        self.assertEqual(actual, expected)
        str_output.close()
        pass


class AllYourBaseTest(unittest.TestCase):

    def test_example(self):
        solver = cj.AllYourBase(PROJECT_HOME + "/data/AllYourBase.txt")
        str_output = StringIO.StringIO()
        solver.solve(output=str_output)
        actual = str_output.getvalue()
        expected = ("Case #1: 201\n"
                    "Case #2: 75\n"
                    "Case #3: 11\n")
        self.assertEqual(actual, expected)
        str_output.close()
        pass

    def test_small_input(self):
        solver = cj.AllYourBase(PROJECT_HOME + "/data/A-small-practice.in")
        with open("out.txt", "w") as f:
            solver.solve(output=f)
        pass

    def test_large_input(self):
        solver = cj.AllYourBase(PROJECT_HOME + "/data/A-large-practice.in")
        with open("out.txt", "w") as f:
            solver.solve(output=f)
        pass


class CenterOfMassTest(unittest.TestCase):

    def test_example(self):
        solver = cj.CenterOfMass(PROJECT_HOME + "/data/CenterOfMass.txt")
        solver.solve()

    def test_small_input(self):
        solver = cj.CenterOfMass(PROJECT_HOME + "/data/B-small-practice.in")
        with open("out.txt", "w") as f:
            solver.solve(output=f)
        pass

    def test_large_input(self):
        solver = cj.CenterOfMass(PROJECT_HOME + "/data/B-large-practice.in")
        with open("out.txt", "w") as f:
            solver.solve(output=f)
        pass


if __name__ == "__main__":
    unittest.main()
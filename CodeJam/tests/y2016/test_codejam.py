
import unittest
import StringIO
import time

import practice.y2016.codejam as cj
import codejam.y2016.codejam as real

PROJECT_HOME = "/Users/cdongsi/Hub/python/CodeJam"


class GetDigitsTest(unittest.TestCase):

    def test_solve(self):
        solver = real.GetDigits(PROJECT_HOME + "/data/GetDigits.txt")
        self.assertEqual("122222", solver._solve_digits("TTWONWTWOOOOTWWEOT") )
        self.assertEqual("2889", solver._solve_digits("GEENIOIITETTNGWHH") )

    def test_example(self):
        solver = real.GetDigits(PROJECT_HOME + "/data/A-small-attempt0.in")

        solver.solve()

        # str_output = StringIO.StringIO()
        # solver.solve(output=str_output)
        # actual = str_output.getvalue()
        # expected = ("Case #1: 4\n"
        #             "Case #2: 3\n"
        #             "Case #3: 3\n"
        #             "Case #4: 6\n")
        # self.assertEqual(actual, expected)
        #
        # str_output.close()
        pass


class BffTest(unittest.TestCase):

    def test_example(self):
        solver = real.Bff(PROJECT_HOME + "/data/BFF.txt")
        str_output = StringIO.StringIO()

        solver.solve(output=str_output)
        actual = str_output.getvalue()
        expected = ("Case #1: 4\n"
                    "Case #2: 3\n"
                    "Case #3: 3\n"
                    "Case #4: 6\n")
        self.assertEqual(actual, expected)

        str_output.close()
        pass

    def test_small_input(self):
        solver = real.Bff(PROJECT_HOME + "/data/C-small-practice.in")
        with open("out.txt", "w") as f:
            solver.solve(output=f)
        pass

    def test_large_input(self):
        solver = real.Bff(PROJECT_HOME + "/data/C-large-practice.in")
        with open("out.txt", "w") as f:
            start = time.clock()
            solver.solve(output=f)
            elapsed = time.clock() - start
            print elapsed
        pass


class LastWordTest(unittest.TestCase):

    def test_example(self):
        solver = real.LastWord(PROJECT_HOME + "/data/LastWord.txt")
        solver.solve()


class CoinJamTest(unittest.TestCase):

    def test_example(self):
        solver = real.CoinJam(PROJECT_HOME + "/data/CoinJam.txt")
        solver.solve()


class RevengeOfPancakes(unittest.TestCase):

    def test_example(self):
        solver = real.RevengeOfPancakes(PROJECT_HOME + "/data/RevengeOfPancakes.txt")
        solver.solve()

    def test_small_input(self):
        solver = real.RevengeOfPancakes(PROJECT_HOME + "/data/A-small-attempt0.in")
        with open("out.txt", "w") as f:
            solver.solve(output=f)
        pass

    def test_large_input(self):
        solver = real.RevengeOfPancakes(PROJECT_HOME + "/data/A-large.in")
        with open("out.txt", "w") as f:
            solver.solve(output=f)
        pass


class CountingSheepTest(unittest.TestCase):

    def test_example(self):
        solver = real.CountingSheep(PROJECT_HOME + "/data/CountingSheep.txt")
        solver.solve()

    def test_small_input(self):
        solver = real.CountingSheep(PROJECT_HOME + "/data/A-small-attempt0.in")
        with open("out.txt", "w") as f:
            solver.solve(output=f)
        pass

    def test_large_input(self):
        solver = real.CountingSheep(PROJECT_HOME + "/data/A-large.in")
        with open("out.txt", "w") as f:
            solver.solve(output=f)
        pass


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
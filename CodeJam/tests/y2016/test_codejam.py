
import unittest
import StringIO
import time
from collections import Counter

import practice.y2016.codejam as cj
import codejam.y2016.codejam as real

PROJECT_HOME = "/Users/cdongsi/Hub/python/CodeJam"


class GetDigitsTest(unittest.TestCase):

    def test_solve(self):
        solver = real.GetDigits(PROJECT_HOME + "/data/GetDigits.txt")
        self.assertEqual("122222", solver._solve_digits("TTWONWTWOOOOTWWEOT") )
        self.assertEqual("2889", solver._solve_digits("GEENIOIITETTNGWHH"))

    @unittest.skip("Experiments to find solution")
    def test_experiment(self):
        solver = real.GetDigits(PROJECT_HOME + "/data/GetDigits.txt")
        counter = Counter()
        for word in real.GetDigits.WORDS:
            for c in word:
                counter[c] += 1

        char_to_digit = {"Z" : 0, "W" : 2, "U": 4, "X": 6, "G": 8}
        remove_digits = []
        for key in counter:
            # print key, counter[key]
            if counter[key] == 1:
                remove_digits.append(key)

        for key_char in remove_digits:
            print key_char
            word_count = solver.counters[char_to_digit[key_char]]
            # print word_count
            counter.subtract(word_count)

        char_to_digit2 = {"R": 3, "F": 5, "S" : 7}
        remove_digits = []
        for key in counter:
            if counter[key] == 1:
                remove_digits.append(key)

        for key_char in char_to_digit2.keys():
            print key_char
            word_count = solver.counters[char_to_digit2[key_char]]
            # print word_count
            counter.subtract(word_count)

        print counter

    def test_example(self):
        solver = real.GetDigits(PROJECT_HOME + "/data/GetDigits.txt")

        str_output = StringIO.StringIO()
        solver.solve(output=str_output)
        actual = str_output.getvalue()
        expected = ("Case #1: 012\n"
                    "Case #2: 2468\n"
                    "Case #3: 114\n"
                    "Case #4: 3\n")
        self.assertEqual(actual, expected)

        str_output.close()
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
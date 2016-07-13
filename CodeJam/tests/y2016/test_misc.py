
import unittest
import practice.y2016.dp as dp
import practice.y2016.misc as ms


class TestSkyline(unittest.TestCase):

    def test_debug(self):
        buildings = [(2, 5, 5), (5, 8, 8), (2, 8, 3)]
        skyline = [(2, 5), (5, 8), (8, 0)]
        self.assertEqual(ms.solve_skyline(buildings), skyline)
        pass

    def test_inout(self):
        buildings = [(2, 9, 10), (3, 6, 15), (5, 12, 12), (13, 16, 10), (13, 16, 10), (15, 17, 5)]
        skyline = [(2, 10), (3, 15), (6, 12), (12, 0), (13, 10), (16, 5), (17, 0)]
        self.assertEqual(ms.solve_skyline(buildings), skyline)

        buildings = [(2, 9, 10), (3, 7, 15), (5, 12, 12), (15, 20, 10), (19, 24, 8)]
        skyline = [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10), (20, 8), (24, 0)]
        self.assertEqual(ms.solve_skyline(buildings), skyline)

        buildings = [(1, 5, 11), (2, 7, 6), (3, 9, 13), (12, 16, 7), (14, 25, 3), (19, 22, 18), (23, 29, 13), (24, 28, 4)]
        skyline = [(1, 11), (3, 13), (9, 0), (12, 7), (16, 3), (19, 18), (22, 3), (23, 13), (29, 0)]
        self.assertEqual(ms.solve_skyline(buildings), skyline)

        """ Test case from http://www.geeksforgeeks.org/divide-and-conquer-set-7-the-skyline-problem/
        """
        buildings_wrong = [(1,11,5), (2,6,7), (3,13,9), (12,7,16), (14,3,25), (19,18,22), (23,13,29), (24,4,28)]
        buildings = [(building[0], building[2], building[1]) for building in buildings_wrong]
        skyline = [(1, 11), (3, 13), (9, 0), (12, 7), (16, 3), (19, 18), (22, 3), (23, 13), (29, 0)]
        self.assertEqual(ms.solve_skyline(buildings), skyline)
        pass

    def test_corner_cases(self):
        # One building completely overlap on the other
        buildings = [(2, 5, 5), (2, 5, 9)]
        skyline = [(2, 9), (5, 0)]
        self.assertEqual(ms.solve_skyline(buildings), skyline)

        # One building is right next to the other
        buildings = [(2, 5, 5), (5, 8, 8)]
        skyline = [(2, 5), (5, 8), (8, 0)]
        self.assertEqual(ms.solve_skyline(buildings), skyline)

        buildings = [(2, 5, 5), (5, 8, 8), (2, 8, 10)]
        skyline = [(2, 10), (8, 0)]
        self.assertEqual(ms.solve_skyline(buildings), skyline)

        buildings = [(2, 5, 5), (5, 8, 8), (2, 8, 3)]
        skyline = [(2, 5), (5, 8), (8, 0)]
        self.assertEqual(ms.solve_skyline(buildings), skyline)
        pass


class TestCode(unittest.TestCase):

    def test_merge_k_lists(self):
        lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(ms.merge_sorted_lists(*lists), range(1, 10))

        lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(ms.merge_sorted_lists(*lists), range(1, 10))

        lists = [[1, 1], [2, 2], [3, 3]]
        self.assertEqual(ms.merge_sorted_lists(*lists), [1, 1, 2, 2, 3, 3])

        lists = [[1, 2, 3], [1, 2, 3]]
        self.assertEqual(ms.merge_sorted_lists(*lists), [1, 1, 2, 2, 3, 3])
        pass

    def test_merge_intervals(self):
        mlist = [(4, 6), (5, 8), (20, 25)]
        expected = [(4, 8), (20, 25)]
        self.assertEqual(expected, ms.combine_intervals(mlist))

        mlist = [(4, 6), (5, 8), (20, 25), (25, 26)]
        expected = [(4, 8), (20, 26)]
        self.assertEqual(expected, ms.combine_intervals(mlist))

        mlist = [(4, 6), (5, 8), (4, 25), (25, 26)]
        expected = [(4, 26)]
        self.assertEqual(expected, ms.combine_intervals(mlist))

        mlist = [(4, 6), (5, 8), (4, 5), (25, 26)]
        expected = [(4, 8), (25, 26)]
        self.assertEqual(expected, ms.combine_intervals(mlist))

        mlist = [(4, 6), (5, 8), (3, 5), (25, 26)]
        expected = [(3, 8), (25, 26)]
        self.assertEqual(expected, ms.combine_intervals(mlist))

        mlist = [(4, 6), (7, 8), (5, 7), (25, 26)]
        expected = [(4, 8), (25, 26)]
        self.assertEqual(expected, ms.combine_intervals(mlist))

        mlist = [(4, 6), (7, 8), (4, 26), (5, 7), (25, 26)]
        expected = [(4, 26)]
        self.assertEqual(expected, ms.combine_intervals(mlist))

        pass


class TestSkylineTracker(unittest.TestCase):

    def test_output(self):
        """ Test SkylineTracker based on PriorityQueue tests.

        :return:
        """

        queue = ms.SkylineTracker()
        queue.add_building("Write code", 5)
        self.assertEqual((5, "Write code"), queue.peek_building())
        queue.add_building("Write spec", 7)
        self.assertEqual((7, "Write spec"), queue.peek_building())
        queue.add_building("Create tests", 3)
        self.assertEqual((7, "Write spec"), queue.peek_building())
        queue.add_building("Write user docs", 1)
        self.assertEqual((7, "Write spec"), queue.peek_building())

        task = queue.pop_building()
        self.assertEqual(task[1], "Write spec")
        self.assertEqual((5, "Write code"), queue.peek_building())

        # Update priority of "Create tests"
        queue.add_building("Create tests", 6)
        self.assertEqual((6, "Create tests"), queue.peek_building())
        task = queue.pop_building()
        self.assertEqual(task[1], "Create tests")

        # Remove task "Write user docs"
        queue.remove_building("Write user docs")
        self.assertEqual((5, "Write code"), queue.peek_building())

        task = queue.pop_building()
        self.assertEqual(task[1], "Write code")
        self.assertEqual(None, queue.peek_building())


class TestMisc(unittest.TestCase):

    def test_rearrange(self):
        self.assertEqual(dp.rearrange("AAB"), "ABA")
        self.assertEqual(dp.rearrange("AAA"), None)
        self.assertEqual(dp.rearrange("AABBCC"), "ACBACB")
        self.assertEqual(dp.rearrange("AABBCCCC"), "CACBCACB")

    def test_stuffs(self):

        id_string = """
1347909198
1347909202
1348160356
1348431422
1349160930
1350585352
1351584783
1351658772
1352159876
1352159878
1353659037
1353659040
"""

        ids = id_string.split()
        ids_int = [str(e) for e in ids]
        print ', '.join(ids_int)

    def test_columns(self):
        table_name = "i"
        column_string = "poid_db,poid_id0,poid_type"
        columns = column_string.split(",")
        columns_with_table = [table_name + "." + e for e in columns]
        print ', '.join(columns_with_table)
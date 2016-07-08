
import unittest
import practice.y2016.dp as dp
import practice.y2016.misc as ms


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

        pass


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
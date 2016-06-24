
import unittest
import practice.y2016.dp as dp


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
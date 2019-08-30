import unittest

from src import compare_version


class TestCompareVersions(unittest.TestCase):
    def test_compare_same_version(self):
        version1 = '1'
        version2 = '1'
        self.assertEqual(compare_version(version1, version2), 0)

    def test_with_lower_version(self):
        version1 = '2.1'
        version2 = '2.2'
        self.assertLess(compare_version(version1, version2), 0)

    def test_with_large_versions(self):
        version1 = "3.0.4.10"
        version2 = "3.0.4.2"
        self.assertGreater(compare_version(version1, version2), 0)

    def test_unequal_lenght_versions(self):
        version1 = "4.08"
        version2 = "4.08.01"
        self.assertLess(compare_version(version1, version2), 0)

    def test_unequal_lenght_versions_case2(self):
        version1 = "3.2.1.9.8144"
        version2 = "3.2"
        self.assertGreater(compare_version(version1, version2), 0)

    def test_with_prefix_zero_after_decimal_point(self):
        version1 = "12.01"
        version2 = "12.1"
        self.assertEqual(compare_version(version1, version2), 0)

    def test_with_one_version_after_decimal_point(self):
        version1 = "1.0"
        version2 = "1"
        self.assertEqual(compare_version(version1, version2), 0)

    def test_with_one_version_after_decimal_point_case2(self):
        version1 = "1"
        version2 = "1.0"
        self.assertEqual(compare_version(version1, version2), 0)

    def test_with_unequal_decimal_point(self):
        version1 = "1.1.3"
        version2 = "1.1.3.000"
        self.assertEqual(compare_version(version1, version2), 0)

    def test_version_extra_zero_after_decimal_point(self):
        version1 = "1.1"
        version2 = "1.10"
        self.assertLess(compare_version(version1, version2), 0)



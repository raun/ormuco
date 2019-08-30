import unittest

from src.overlap import Interval, is_overlap_internal
from src import is_overlap


class TestInterval(unittest.TestCase):

    def test_positive_points(self):
        points = (1, 5)
        interval = Interval(*points)
        self.assertEqual(interval.get_start(), min(points))
        self.assertEqual(interval.get_end(), max(points))

    def test_negative_points(self):
        points = (-1, -5)
        interval = Interval(*points)
        self.assertEqual(interval.get_start(), min(points))
        self.assertEqual(interval.get_end(), max(points))

    def test_positive_negative(self):
        points = (-1, 5)
        interval = Interval(*points)
        self.assertEqual(interval.get_start(), min(points))
        self.assertEqual(interval.get_end(), max(points))

    def test_out_of_order_points(self):
        points = (5, -1)
        interval = Interval(*points)
        self.assertEqual(interval.get_start(), min(points))
        self.assertEqual(interval.get_end(), max(points))
        self.assertTrue(interval.get_start() <= interval.get_end())

    def test_more_than_2_points(self):
        points = (5, -1, 3)
        with self.assertRaises(OverflowError):
            Interval(*points)

    def test_interval_str(self):
        points = (1, 5)
        interval = Interval(*points)
        self.assertEqual(str(interval), "({}, {})".format(interval.get_start(), interval.get_end()))
        self.assertEqual(repr(interval), "({}, {})".format(interval.get_start(), interval.get_end()))


class TestIsOverlapInternal(unittest.TestCase):
    def test_with_possible_overlap(self):
        point1 = (1, 5)
        point2 = (2, 6)
        interval1 = Interval(*point1)
        interval2 = Interval(*point2)
        self.assertTrue(is_overlap_internal(interval1, interval2))

    def test_with_points_reverse_order(self):
        point1 = (2, 6)
        point2 = (1, 5)
        interval1 = Interval(*point1)
        interval2 = Interval(*point2)
        self.assertTrue(is_overlap_internal(interval1, interval2))

    def test_with_no_overlap(self):
        point1 = (1, 5)
        point2 = (6, 8)
        interval1 = Interval(*point1)
        interval2 = Interval(*point2)
        self.assertFalse(is_overlap_internal(interval1, interval2))

    def test_with_negative_points_with_overlap(self):
        point1 = (-1, -5)
        point2 = (-2, -6)
        interval1 = Interval(*point1)
        interval2 = Interval(*point2)
        self.assertTrue(is_overlap_internal(interval1, interval2))

    def test_with_overlap_in_opposite_direction(self):
        point1 = (-1, -5)
        point2 = (-2, 6)
        interval1 = Interval(*point1)
        interval2 = Interval(*point2)
        self.assertTrue(is_overlap_internal(interval1, interval2))

    def test_with_negative_points_with_no_overlap(self):
        point1 = (-1, -5)
        point2 = (-6, 8)
        interval1 = Interval(*point1)
        interval2 = Interval(*point2)
        self.assertTrue(is_overlap_internal(interval1, interval2))

    def test_with_points_that_are_subset(self):
        point1 = (1, 5)
        point2 = (0, 6)
        interval1 = Interval(*point1)
        interval2 = Interval(*point2)
        self.assertTrue(is_overlap_internal(interval1, interval2))

    def test_with_touching_interval(self):
        point1 = (1, 5)
        point2 = (5, 8)
        interval1 = Interval(*point1)
        interval2 = Interval(*point2)
        self.assertFalse(is_overlap_internal(interval1, interval2))


class TestIsOverlap(unittest.TestCase):
    def test_with_possible_overlap(self):
        self.assertTrue(is_overlap(1, 5, 2, 6))

    def test_with_points_reverse_order(self):
        self.assertTrue(is_overlap(2, 6, 1, 5))

    def test_with_no_overlap(self):
        self.assertFalse(is_overlap(1, 5, 6, 8))

    def test_with_negative_points_with_overlap(self):
        self.assertTrue(is_overlap(-1, -5, -2, -6))

    def test_with_overlap_in_opposite_direction(self):
        self.assertTrue(is_overlap(-1, -5, -2, 6))

    def test_with_negative_points_with_no_overlap(self):
        self.assertTrue(is_overlap(-1, -5, -6, 8))

    def test_with_points_that_are_subset(self):
        self.assertTrue(is_overlap(1, 5, 0, 6))

    def test_with_touching_interval(self):
        self.assertFalse(is_overlap(1, 5, 5, 8))

    def test_with_possible_overlap_with_floating_points(self):
        self.assertTrue(is_overlap(1.5, 5, 2, 5.5))

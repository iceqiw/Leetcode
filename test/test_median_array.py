from unittest import TestCase

from src.median_array import Solution


class TestSolution(TestCase):
    def test_find_median_sorted_arrays(self):
        m = Solution()
        median = m.findMedianSortedArrays([1, 2], [3, 4])
        self.assertEqual(2.5, median)

    def test_find_median_sorted_arrays2(self):
        m = Solution()
        median = m.findMedianSortedArrays([1, 2], [3, 4, 5])
        self.assertEqual(3, median)

    def test_find_median_sorted_arrays3(self):
        m = Solution()
        median = m.findMedianSortedArrays([1, 3], [2])
        self.assertEqual(2, median)

    def test_find_median_sorted_arrays4(self):
        m = Solution()
        median = m.findMedianSortedArrays([], [1])
        self.assertEqual(1, median)
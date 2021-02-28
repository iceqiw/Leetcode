from unittest import TestCase

from src.maxlen import Solution


class TestSolution(TestCase):
    def test_length_of_longest_substring(self):
        m = Solution()
        out = m.lengthOfLongestSubstring("pwwkew")
        self.assertEqual(out, 3)

    def test_length_of_longest_substring2(self):
        m = Solution()
        out = m.lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(out, 3)

    def test_length_of_longest_substring3(self):
        m = Solution()
        out = m.lengthOfLongestSubstring(" ")
        self.assertEqual(out, 1)

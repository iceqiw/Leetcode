from unittest import TestCase

from src.CourseSchedule import Solution


class TestSolution(TestCase):
    def test_can_finish(self):
        m = Solution()
        is_finish = m.canFinish(2, [[1, 0]])
        self.assertEqual(is_finish, True)

    def test_can_finish1(self):
        m = Solution()
        is_finish = m.canFinish(2, [[0, 1]])
        self.assertEqual(is_finish, True)

    def test_can_finish2(self):
        m = Solution()
        is_finish = m.canFinish(2, [[1, 0], [0, 1]])
        self.assertEqual(is_finish, False)

    def test_can_finish3(self):
        m = Solution()
        is_finish = m.canFinish(3, [[1, 0], [1, 2], [0, 1]])
        self.assertEqual(is_finish, False)

    def test_can_finish4(self):
        m = Solution()
        is_finish = m.canFinish(8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]])
        self.assertEqual(is_finish, True)

from unittest import TestCase

from src.primeNumbers import Solution


class TestSolution(TestCase):
    def test_count_primes(self):
        m = Solution()
        length = m.countPrimes(10)
        self.assertEqual(4, length)

    def test_count_primes2(self):
        m = Solution()
        length = m.countPrimes(1)
        self.assertEqual(0, length)

    def test_count_primes3(self):
        m = Solution()
        length = m.countPrimes(2)
        self.assertEqual(0, length)

    def test_count_primes4(self):
        m = Solution()
        length = m.countPrimes(499979)
        self.assertEqual(41537, length)

    def test_count_primes5(self):
        m = Solution()
        length = m.countPrimes(7)
        self.assertEqual(3, length)

    def test_count_primes6(self):
        m = Solution()
        length = m.countPrimes(12)
        self.assertEqual(5, length)

    def test_count_primes7(self):
        m = Solution()
        length = m.countPrimes(6)
        self.assertEqual(3, length)

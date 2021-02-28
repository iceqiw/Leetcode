import math


class Solution:
    def __init__(self):
        self.primes = [2, 3]

    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        if n == 3:
            return 1
        if n <= 5:
            return 2
        count = 2
        for i in range(6, n + 1, 6):
            count = count + self.isPrimes(i, n)
        return count

    def isPrimes(self, k, n):
        sqrt = int(math.sqrt(k)) + 1
        x = 1
        y = 1
        i = 3

        while i <= sqrt:
            if (k + 1) >= n or (k + 1) % i == 0:
                y = 0
            if (k - 1) % i == 0:
                x = 0
            i = i + 2

        # for i in self.primes:
        #     if i > sqrt + 1:
        #         break
        #     if y % i == 0:
        #         y = 0
        #     if x % i == 0:
        #         x = 0
        return x + y

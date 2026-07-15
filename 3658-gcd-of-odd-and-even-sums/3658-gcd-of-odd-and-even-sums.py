from math import gcd

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # Formula for sum of first n odd numbers:
        # 1 + 3 + 5 + ... + (2n-1) = n^2
        sumOdd = n * n

        # Formula for sum of first n even numbers:
        # 2 + 4 + 6 + ... + (2n) = n(n+1)
        sumEven = n * (n + 1)

        # Return the greatest common divisor of the two sums
        return gcd(sumOdd, sumEven)

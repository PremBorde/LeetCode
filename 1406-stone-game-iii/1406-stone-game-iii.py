from functools import cache

class Solution:
    s = ["Bob", "Tie", "Alice"]

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @cache
        def maxDiff(i):
            if i == n:
                return 0

            a = b = c = -10**9

            if i < n:
                a = stoneValue[i] - maxDiff(i + 1)

            if i + 1 < n:
                b = stoneValue[i] + stoneValue[i + 1] - maxDiff(i + 2)

            if i + 2 < n:
                c = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - maxDiff(i + 3)

            return max(a, b, c)

        d = maxDiff(0)
        return self.s[(d > 0) - (d < 0) + 1]
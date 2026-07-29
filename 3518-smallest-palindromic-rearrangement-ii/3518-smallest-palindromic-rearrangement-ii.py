class Solution:
    LIMIT = 1000000

    # Calculate nCr (capped at LIMIT+1 to avoid huge numbers)
    def combCapped(self, n, r):
        if r < 0 or r > n:
            return 0

        # nCr == nC(n-r)
        r = min(r, n - r)

        if r == 0:
            return 1

        res = 1

        for i in range(1, r + 1):
            res = res * (n - r + i) // i

            # No need to calculate beyond LIMIT
            if res > self.LIMIT:
                return self.LIMIT + 1

        return res

    # Count total distinct permutations
    def countWays(self, cnt):
        remaining = sum(cnt)
        ans = 1

        for c in cnt:
            if c == 0:
                continue

            part = self.combCapped(remaining, c)
            ans *= part

            if ans > self.LIMIT:
                return self.LIMIT + 1

            remaining -= c

        return ans

    def smallestPalindrome(self, s: str, k: int) -> str:

        # Frequency of characters
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        half = [0] * 26
        mid = ""
        length = 0

        # Build half frequencies
        for i in range(26):
            half[i] = freq[i] // 2
            length += half[i]

            if freq[i] % 2:
                mid = chr(i + ord('a'))

        # Total palindromes less than k
        if self.countWays(half) < k:
            return ""

        left = []

        # Build left half greedily
        for _ in range(length):

            for ch in range(26):

                if half[ch] == 0:
                    continue

                # Try taking this character
                half[ch] -= 1

                ways = self.countWays(half)

                if ways >= k:
                    left.append(chr(ch + ord('a')))
                    break

                # Skip these permutations
                k -= ways

                # Restore frequency
                half[ch] += 1

        left = "".join(left)

        # Mirror left part
        right = left[::-1]

        return left + mid + right
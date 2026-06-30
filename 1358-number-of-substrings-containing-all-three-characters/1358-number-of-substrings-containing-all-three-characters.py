class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        # Last seen positions of a, b and c
        last = [-1, -1, -1]

        ans = 0

        for i, ch in enumerate(s):

            # Update last occurrence
            last[ord(ch) - ord('a')] = i

            # Earliest occurrence among a,b,c
            ans += min(last) + 1

        return ans
        
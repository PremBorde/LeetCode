class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        # Add virtual 1's at both ends
        t = "1" + s + "1"

        base = s.count("1")      # Current active sections
        ans = base

        n = len(t)
        i = 1

        while i < n - 1:

            # Find a block of 1's
            if t[i] == '1':
                start = i
                while i < n - 1 and t[i] == '1':
                    i += 1
                end = i - 1

                # Valid only if surrounded by 0's
                if t[start - 1] == '0' and t[end + 1] == '0':
                    # Count consecutive 0's on left
                    left = 0
                    j = start - 1
                    while t[j] == '0':
                        left += 1
                        j -= 1
                    # Count consecutive 0's on right
                    right = 0
                    j = end + 1
                    while t[j] == '0':
                        right += 1
                        j += 1
                    # Net increase = left zeros + right zeros
                    ans = max(ans, base + left + right)
            else:
                i += 1

        return ans
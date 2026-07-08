class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # pow10[i] = 10^i % MOD
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # Prefix count of non-zero digits
        cnt = [0] * (n + 1)

        # Prefix sum of non-zero digits
        digit_sum = [0] * (n + 1)

        # Prefix value of concatenated non-zero digits
        value = [0] * (n + 1)

        for i in range(n):
            cnt[i + 1] = cnt[i]
            digit_sum[i + 1] = digit_sum[i]
            value[i + 1] = value[i]

            if s[i] != '0':
                d = int(s[i])

                cnt[i + 1] += 1
                digit_sum[i + 1] += d

                # Append digit to the current number
                value[i + 1] = (value[i] * 10 + d) % MOD

        ans = []

        for l, r in queries:

            # Number of non-zero digits
            c = cnt[r + 1] - cnt[l]

            # No non-zero digits
            if c == 0:
                ans.append(0)
                continue

            # Sum of digits
            sm = digit_sum[r + 1] - digit_sum[l]

            # Extract concatenated number modulo MOD
            num = (
                value[r + 1]
                - value[l] * pow10[c]
            ) % MOD

            ans.append((num * sm) % MOD)

        return ans
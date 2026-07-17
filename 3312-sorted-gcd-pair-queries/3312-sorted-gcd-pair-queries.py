from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:

        mx = max(nums)

        # freq[x] = frequency of value x
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # exact[g] = number of pairs whose GCD is exactly g
        exact = [0] * (mx + 1)

        # Process GCDs from largest to smallest
        for g in range(mx, 0, -1):

            cnt = 0

            # Count numbers divisible by g
            for multiple in range(g, mx + 1, g):
                cnt += freq[multiple]

                # Remove pairs already counted for larger GCDs
                exact[g] -= exact[multiple]

            # Total pairs divisible by g
            exact[g] += cnt * (cnt - 1) // 2

        # Prefix sum
        prefix = [0] * (mx + 1)
        for i in range(1, mx + 1):
            prefix[i] = prefix[i - 1] + exact[i]

        ans = []

        # Binary search answer for each query
        for q in queries:
            ans.append(bisect_right(prefix, q))

        return ans
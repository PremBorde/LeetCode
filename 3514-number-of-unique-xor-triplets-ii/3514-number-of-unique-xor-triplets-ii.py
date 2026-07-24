class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:

        # Maximum possible XOR value is always < 2 * max(nums)
        mx = max(nums) << 1      # Same as max(nums) * 2

        # st[x] = True if x can be obtained as XOR of any two numbers
        st = [False] * mx

        # Compute every possible XOR of two elements
        for a in nums:
            for b in nums:
                st[a ^ b] = True

        # seen[x] = 1 if x can be obtained as XOR of three elements
        seen = [0] * mx

        # Try every (a ^ b) with every third element c
        for ab in range(mx):
            if st[ab]:
                for c in nums:
                    seen[ab ^ c] = 1

        # Count distinct XOR values
        return sum(seen)
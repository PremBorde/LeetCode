from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_num = max(nums)

        # Special case for 1
        if 1 in cnt:
            ans = cnt[1] if cnt[1] % 2 else cnt[1] - 1
        else:
            ans = 1

        for num in nums:
            if num == 1:
                continue

            length = 0
            x = num

            # Every non-center value must appear at least twice
            while x <= max_num and x in cnt and cnt[x] >= 2:
                length += 2
                x *= x

            # If x exists, it can be the center (+1)
            # Otherwise previous value becomes center (-1)
            if x in cnt:
                ans = max(ans, length + 1)
            else:
                ans = max(ans, length - 1)

        return ans
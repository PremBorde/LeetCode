from typing import List
from bisect import bisect_left, bisect_right


class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        if self.n == 0:
            self.seg = []
            return

        self.seg = [0] * (4 * self.n)
        self.arr = nums
        self.build(1, 0, self.n - 1)

    def build(self, node, l, r):
        if l == r:
            self.seg[node] = self.arr[l]
            return

        mid = (l + r) // 2
        self.build(node * 2, l, mid)
        self.build(node * 2 + 1, mid + 1, r)

        self.seg[node] = max(self.seg[node * 2], self.seg[node * 2 + 1])

    def query_util(self, node, st, en, l, r):
        if l <= st and en <= r:
            return self.seg[node]

        mid = (st + en) // 2
        ans = 0

        if l <= mid:
            ans = max(ans, self.query_util(node * 2, st, mid, l, r))

        if r > mid:
            ans = max(ans, self.query_util(node * 2 + 1, mid + 1, en, l, r))

        return ans

    def query(self, l, r):
        if self.n == 0 or l > r:
            return 0

        return self.query_util(1, 0, self.n - 1, l, r)


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:

        n = len(s)
        totalOnes = s.count('1')

        zeroBlocks = []
        zeroLeft = []
        zeroRight = []

        i = 0
        while i < n:
            j = i

            while j < n and s[j] == s[i]:
                j += 1

            if s[i] == '0':
                zeroBlocks.append(j - i)
                zeroLeft.append(i)
                zeroRight.append(j - 1)

            i = j

        m = len(zeroBlocks)

        if m <= 1:
            return [totalOnes] * len(queries)

        nums = []

        for i in range(m - 1):
            nums.append(zeroBlocks[i] + zeroBlocks[i + 1])

        seg = SegmentTree(nums)

        ans = []

        for l, r in queries:

            l_idx = bisect_left(zeroRight, l)
            r_idx = bisect_right(zeroLeft, r) - 1

            if l_idx > m - 1 or r_idx < 0 or l_idx >= r_idx:
                ans.append(totalOnes)
                continue

            leftLen = zeroRight[l_idx] - max(zeroLeft[l_idx], l) + 1

            rightLen = min(r, zeroRight[r_idx]) - zeroLeft[r_idx] + 1

            if l_idx + 1 == r_idx:
                ans.append(totalOnes + leftLen + rightLen)
                continue

            leftContri = leftLen + zeroBlocks[l_idx + 1]

            rightContri = rightLen + zeroBlocks[r_idx - 1]

            middleContri = seg.query(l_idx + 1, r_idx - 2)

            ans.append(
                totalOnes +
                max(leftContri, rightContri, middleContri)
            )

        return ans
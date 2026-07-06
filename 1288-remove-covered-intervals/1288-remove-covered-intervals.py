class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        # Sort intervals:
        # 1. Start point in ascending order.
        # 2. If starts are equal, larger end comes first.
        # Example:
        # [1,4], [1,3], [2,8]
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0                 # Number of intervals remaining
        max_end = 0               # Largest end seen so far

        # Traverse every interval
        for start, end in intervals:

            # If current interval ends before or at max_end,
            # it is completely covered by a previous interval.
            if end <= max_end:
                continue

            # Otherwise, this interval is not covered.
            count += 1

            # Update the farthest ending point seen.
            max_end = end

        return count
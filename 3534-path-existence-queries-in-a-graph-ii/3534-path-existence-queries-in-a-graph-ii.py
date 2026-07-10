class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        LOG = 20  # Since 2^20 > 1e5

        # Store (value, original_index)
        pairs = sorted((nums[i], i) for i in range(n))

        # jump[i][k] = node reached after 2^k jumps
        jump = [[0] * LOG for _ in range(n)]

        r = n - 1

        # Build first jump table
        for l in range(n - 1, -1, -1):

            # Shrink window until values differ by <= maxDiff
            while pairs[r][0] - pairs[l][0] > maxDiff:
                r -= 1

            original_node = pairs[l][1]
            farthest_node = pairs[r][1]

            jump[original_node][0] = farthest_node

            # Binary lifting table
            for k in range(1, LOG):
                jump[original_node][k] = jump[jump[original_node][k - 1]][k - 1]

        ans = []

        for u, v in queries:

            # Always move from smaller value to larger value
            if nums[u] > nums[v]:
                u, v = v, u

            # Same node
            if u == v:
                ans.append(0)
                continue

            # Same value => directly connected
            if nums[u] == nums[v]:
                ans.append(1)
                continue

            distance = 0

            # Jump as far as possible without crossing target value
            for k in range(LOG - 1, -1, -1):

                if nums[jump[u][k]] < nums[v]:
                    distance += 1 << k
                    u = jump[u][k]

            # Cannot reach target
            if nums[jump[u][0]] < nums[v]:
                ans.append(-1)

            # One final jump reaches target
            else:
                ans.append(distance + 1)

        return ans
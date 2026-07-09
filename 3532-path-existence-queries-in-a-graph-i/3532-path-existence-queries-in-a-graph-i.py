class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        # component[i] = Connected component number of node i
        component = [0] * n

        comp = 0

        # Build connected components
        for i in range(1, n):

            # If current and previous cannot connect,
            # start a new component
            if nums[i] - nums[i - 1] > maxDiff:
                comp += 1

            component[i] = comp

        ans = []

        # Same component => path exists
        for u, v in queries:
            ans.append(component[u] == component[v])

        return ans
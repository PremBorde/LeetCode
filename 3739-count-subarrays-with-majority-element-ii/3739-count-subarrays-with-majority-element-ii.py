class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # Step 1: Transform array
        arr = [1 if x == target else -1 for x in nums]
        
        # Step 2: Prefix sums
        prefix = [0]
        for x in arr:
            prefix.append(prefix[-1] + x)
        
        # Step 3: Coordinate compression
        sorted_prefix = sorted(set(prefix))
        index = {v: i for i, v in enumerate(sorted_prefix)}
        
        # Fenwick Tree
        fenwick = [0] * (len(sorted_prefix) + 1)
        
        def update(i):
            i += 1
            while i < len(fenwick):
                fenwick[i] += 1
                i += i & -i
        
        def query(i):
            res = 0
            i += 1
            while i > 0:
                res += fenwick[i]
                i -= i & -i
            return res
        
        ans = 0
        for p in prefix:
            idx = index[p]
            ans += query(idx - 1)   # count earlier prefix sums < current
            update(idx)
        
        return ans

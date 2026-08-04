class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
    # Step 1: Find smallest and largest element in nums
        min_val = min(nums)
        max_val = max(nums)

        # Step 2: Create full range from min to max
        full_range = set(range(min_val, max_val + 1))

        # Step 3: Convert nums to set
        nums_set = set(nums)

        # Step 4: Find missing elements
        missing = sorted(list(full_range - nums_set))

        # Step 5: Return result
        return missing
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        # Special case
        # Product of positive integers can never be < 1
        if k <= 1:
            return 0

        left = 0              # Left pointer of window
        product = 1           # Product of current window
        count = 0             # Total valid subarrays

        # Expand window
        for right in range(len(nums)):

            # Include new element
            product *= nums[right]

            # If window becomes invalid
            while product >= k:

                # Remove left element
                product //= nums[left]

                # Shrink window
                left += 1

            # All subarrays ending at 'right'
            # and starting from left...right are valid
            count += (right - left + 1)

        return count
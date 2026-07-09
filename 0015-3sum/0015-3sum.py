class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()                    # Step 1: Sort array
        ans = []

        for i in range(len(nums)):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1               # Next element
            right = len(nums) - 1      # Last element

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1          # Need bigger sum

                elif total > 0:
                    right -= 1         # Need smaller sum

                else:
                    # Found one triplet
                    ans.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return ans
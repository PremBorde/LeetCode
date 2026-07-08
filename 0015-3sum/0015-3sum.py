class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()          # Required for two pointers
        ans = []

        # Fix first element
        for i in range(len(nums) - 2):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                # Found a triplet
                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # Sum too small → increase it
                elif total < 0:
                    left += 1

                # Sum too large → decrease it
                else:
                    right -= 1

        return ans
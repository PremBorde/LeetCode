class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count = 0      # Current consecutive 1's
        maxi = 0       # Maximum consecutive 1's

        # Traverse pura array
        for num in nums:

            # Agar 1 mila
            if num == 1:
                count += 1              # Count badhao

                # Maximum update karo
                maxi = max(maxi, count)

            else:
                # 0 mila to streak toot gayi
                count = 0

        return maxi
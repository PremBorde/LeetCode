class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total = sum(nums)                            # Total Sum 
        left_sum = 0                                 # LeftSide Sum 
        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]   # RighSide = total - left - currNo.   

            if left_sum == right_sum:                # Sumation of LeftSide == RighSide
                return i                             # Return Index
            left_sum += nums[i]                      # OtherWIse increas LeftSum += num[i]
        return -1
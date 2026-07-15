class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = nums[0]                    # Handle Negative Cases as Well 

        for num in nums: 
            curr_sum += num                   # Sumation of Values 
            max_sum = max(max_sum,curr_sum)   # Maximum value 
            if curr_sum < 0:                  # If negative then 
                curr_sum = 0                  # Reset the value 
        return max_sum
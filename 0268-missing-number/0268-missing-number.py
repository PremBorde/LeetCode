class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2   # FORMULA TO FIND MISSING NUMBER n(n+1)/2
        actual_sum = sum(nums)            # sum of given numbers
        result = expected_sum - actual_sum    # Store the result 
        return result    

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = second_largest = -1
        
        for num in nums:

            # New largest found
            if num > largest:
                second_largest = largest
                largest = num

            # Update second largest
            elif num > second_largest:
                second_largest = num

        # Maximum product
        return (largest - 1) * (second_largest - 1)
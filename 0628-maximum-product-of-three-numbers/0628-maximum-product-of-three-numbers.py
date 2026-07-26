class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        max1 = max2 = max3 = float("-inf")      # Three largest numbers
        min1 = min2 = float("inf")              # Two smallest numbers

        for num in nums:

            if num > max1:                           # Update largest 3 numbers
                max1, max2, max3 = num, max1, max2   # max1 = num 

            elif num > max2:
                max2, max3 = num, max2              # max2 = num

            elif num > max3:        
                max3 = num                          # max3 = num

            if num < min1:                          # Update smallest 2 numbers
                min1, min2 = num, min1              # min1 = num

            elif num < min2:
                min2 = num                          # min2 = num

        product1 = max1 * max2 * max3        # Case 1: Product of 3 largest number
       
        product2 = min1 * min2 * max1       # Case 2: Product of 2 smallest (-Ve) and largest No.
        
        return max(product1, product2)
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []                         # Store GCD 
        maxi = nums[0]                         # Maximum value

        for num in nums:
            maxi = max(maxi , num)              # Update Maximum Value 
            prefixGcd.append(gcd(num,maxi))     # Append using gcd(curr,Max) Function

        prefixGcd.sort()                        # Sort in Ascending Order
        ans = 0                                 # Return Ans -> Int 
        left = 0                                # First 
        right = len(nums) - 1                   # Last 
        
        while left < right :
            ans += gcd(prefixGcd[left],prefixGcd[right] )   # Add First or last -> Ans
            left +=1                                        # Increment left to right 
            right -=1                                       # Decrement Right to left
        return ans
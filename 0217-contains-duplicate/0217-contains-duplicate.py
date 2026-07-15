class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()        # Store Unquie Element (Value not add again)
        for num in nums:     
            if num in seen:             # If found 
                return True             # Return True 
            seen.add(num)               # Add that value 
        return False
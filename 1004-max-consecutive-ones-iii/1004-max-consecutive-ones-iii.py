class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0            # left Pointer
        zero_cnt = 0        # 0s Count 
        n = len(nums)       # Length of Arr
        
        for right in range(n):          # Right Pointer in arr
            if nums[right] == 0:        # If Right Pointer == 0 
                zero_cnt +=1            # Increas 0s Count 
            if zero_cnt > k :
                if nums[left] == 0:     # Invalid 
                    zero_cnt -=1        # Decrease 0s Count
                left +=1                # Increment Left pointer 
        return n - left                 # Remaining Value from left pointer to total length = ANS
 

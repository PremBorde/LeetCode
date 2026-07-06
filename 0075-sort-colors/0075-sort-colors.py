class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0                   # Red = 0     Starting Index
        mid = 0                   # white = 1 - current Index 
        high = len(nums)-1        # Blue = 2 , last Index

        while mid <= high:        
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low] , nums[mid]
                low +=1
                mid +=1
            elif nums[mid] == 1:
                mid +=1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -=1

       
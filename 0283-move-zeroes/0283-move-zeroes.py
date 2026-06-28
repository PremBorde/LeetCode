class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if nums == 0:
            return nums
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[j] = nums[j], nums[i]
                j+=1
        return nums
        
        #write = 0
        #for read in range(len(nums)):
        #   if nums[read] != 0:
        #       nums[write] = nums[read]
        #        write+=1
        
        #while write < len(nums):
        #    nums[write] = 0
        #    write+=1
        #return nums
        
        
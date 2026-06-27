class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1

        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1 ,right+1]
            elif s < target:
                left +=1
            else:
                right -=1
        return [-1,-1]
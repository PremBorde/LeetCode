class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #for ch in letters:
        #    if ch > target:
        #        return ch 
        #return letters[0]

        left, right = 0, len(letters) - 1   # indices of first and last element
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1   # move right, need something greater
            else:
                right = mid - 1  # move left, mid is a candidate
        return letters[left % len(letters)]  # wrap-around
class Solution:
    def largestOddNumber(self, num: str) -> str:
        last = len(num)-1
        for i in range(last,-1,-1):    # Ulta String 
            if int(num[i])% 2 != 0:    # Check Odd INT in String 
                return num[: i+1]      # Return All those String 
        return ""                      # OtherWise Empty String 
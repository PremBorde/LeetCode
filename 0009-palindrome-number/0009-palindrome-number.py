class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # If number is negative then false
            return False
        temp = x    # Kepp the original Number
        rev = 0    
        while x > 0:
            digit = x % 10   # Last digit Extract
            rev = rev * 10 + digit     # Build Reverse the number 
            x //= 10   # Remove last digit x

        return temp == rev

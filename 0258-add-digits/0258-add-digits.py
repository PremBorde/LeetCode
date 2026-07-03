class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            ans = 0
            while num > 0:
                digit = num % 10      # Take last digit
                ans += digit          # Add digit
                num //= 10            # Remove last digit
            num = ans                 # Repeat for new number
        return num
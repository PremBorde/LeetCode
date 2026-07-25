class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        while n > 0:
            digits.append(n % 10)   # extract last digit
            n //= 10                # remove last digit

        max_prod = 0
        for i in range(len(digits)):
            for j in range(i+1,len(digits)):
                max_prod = max(max_prod , digits[i] * digits[j])
        return max_prod
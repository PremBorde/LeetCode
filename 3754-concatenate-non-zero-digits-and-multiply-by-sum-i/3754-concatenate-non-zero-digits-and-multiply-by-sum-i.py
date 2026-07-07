class Solution:
    def sumAndMultiply(self, n: int) -> int:
        concat_num = 0      # will hold the concatenated non-zero digits
        total_sum = 0       # will hold the sum of all digits
        multiplier = 1      # tracks place value (ones, tens, hundreds...)

        # Loop until all digits are processed
        while n > 0:
            digit = n % 10          # extract the last digit
            total_sum += digit      # add digit to total sum

            if digit != 0:          # only use non-zero digits for concatenation
                # Place digit in correct column using multiplier
                # Example: if digit=2 and multiplier=10 → contributes "20"
                concat_num = digit * multiplier + concat_num
                multiplier *= 10    # shift place value left (ones→tens→hundreds)

            n //= 10                # remove the last digit

        # Final result = concatenated non-zero number × sum of all digits
        return concat_num * total_sum

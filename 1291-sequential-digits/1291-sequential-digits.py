class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        ans = []

        # Starting digit can only be from 1 to 9
        for start in range(1, 10):

            num = start          # Current sequential number
            next_digit = start + 1

            # Keep adding next consecutive digit
            while next_digit <= 9:

                # Example:
                # 12 -> 123
                # 123 -> 1234
                num = num * 10 + next_digit

                # If number lies in range, store it
                if low <= num <= high:
                    ans.append(num)

                # If number already exceeded high,
                # no need to continue because it will only become bigger
                if num > high:
                    break

                next_digit += 1

        # Numbers may not be generated in sorted order
        ans.sort()

        return ans
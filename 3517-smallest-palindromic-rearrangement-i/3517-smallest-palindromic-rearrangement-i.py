class Solution:
    def smallestPalindrome(self, s: str) -> str:

        # Count frequency using dictionary
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        left = []
        middle = ""

        # Process characters in alphabetical order
        for ch in sorted(freq):

            # Add half occurrences to left part
            left.append(ch * (freq[ch] // 2))

            # Odd frequency character goes in middle
            if freq[ch] % 2 == 1:
                middle = ch

        # Convert list to string
        left = "".join(left)

        # Mirror the left part
        right = left[::-1]

        return left + middle + right
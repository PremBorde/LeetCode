class Solution:
    def smallestSubsequence(self, s: str) -> str:

        last_index = {}

        # Store last occurrence of every character
        for i, c in enumerate(s):
            last_index[c] = i

        stack = []      # Stores final answer
        seen = set()    # Tracks characters already in stack

        for i, c in enumerate(s):

            # Skip if character already added
            if c in seen:
                continue

            # Remove bigger characters if:
            # 1. Stack is not empty
            # 2. Current char is smaller (lexicographically)
            # 3. Top character appears again later
            while stack and c < stack[-1] and i < last_index[stack[-1]]:
                seen.remove(stack.pop())   # Remove from stack and seen

            # Add current character
            stack.append(c)
            seen.add(c)

        # Convert list -> string
        return "".join(stack)
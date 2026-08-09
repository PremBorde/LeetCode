class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for bracket in s:

            # Opening bracket → push into stack
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)

            else:
                # Closing bracket but nothing to match
                if len(stack) == 0:
                    return False

                # Remove the last opening bracket
                ch = stack.pop()

                # Check if opening and closing brackets match
                if (
                    (bracket == ')' and ch == '(')
                    or
                    (bracket == '}' and ch == '{')
                    or
                    (bracket == ']' and ch == '[')
                ):
                    continue

                # Mismatch → invalid
                else:
                    return False

        # Stack must be empty after processing everything
        return len(stack) == 0
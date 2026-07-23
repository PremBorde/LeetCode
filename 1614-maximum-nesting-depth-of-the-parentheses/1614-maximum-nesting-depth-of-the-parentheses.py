class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0            # Current Number of Parantheses(depth)
        max_depth = 0        # Maximun Nunber of Paranthesese(depth)

        for ch in s:
            if ch == '(':       # IF left Increase Count(depth)
                depth +=1   
                max_depth = max(max_depth,depth)
            else:
                if ch == ')':   # IF Right Decrease Count(depth)
                    depth -=1
        return max_depth        # Return Maximun Count - DEPTH 

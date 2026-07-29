class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!= len(goal):
            return False
        return goal in (s+s) 
        # s+s = abcde + abcde =
        # s = ab cdeab cde
        # goal = cdeab  - goal in s - TRUE 
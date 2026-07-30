class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0

        # i = position of character
        for i in range(len(word)):
            ans += i // 8 + 1

        return ans

        # i = 0..7   → 0//8 + 1 = 1 push
        # i = 8..15  → 8//8 + 1 = 2 pushes    
        # i =16..23  →16//8 + 1 = 3 pushes
        # i =24..25  →24//8 + 1 = 4 pushes    
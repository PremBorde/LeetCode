class Solution:
    def minimumPushes(self, word: str) -> int:

        # Count frequency
        freq = {}

        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1

        # Highest frequency first
        arr = sorted(freq.values(), reverse=True)

        ans = 0

        # Assign push cost
        for i in range(len(arr)):
            ans += arr[i] * (i // 8 + 1)

        return ans
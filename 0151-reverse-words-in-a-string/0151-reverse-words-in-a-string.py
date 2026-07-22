class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()              # split string into list of words
        words.reverse()                # reverse the list in place
        result = " ".join(words)       # join back with spaces
        return result
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m, n = len(word1), len(word2)

        # right[j] = index in word1 used to match word2[j]
        # in the greedy matching from the right.
        right = [-1] * n
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                right[j] = i
                j -= 1
            i -= 1

        ans = []
        i = j = 0
        used = False

        while j < n:
            while i < m:
                if word1[i] == word2[j]:
                    ans.append(i)
                    i += 1
                    j += 1
                    break

                if not used:
                    if j == n - 1 or (right[j + 1] != -1 and right[j + 1] > i):
                        used = True
                        ans.append(i)
                        i += 1
                        j += 1
                        break

                i += 1
            else:
                return []

        return ans
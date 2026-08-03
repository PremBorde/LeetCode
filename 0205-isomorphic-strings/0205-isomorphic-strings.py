class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mp1 = {}
        mp2 = {}
        # Traverse both strings together
        for c1, c2 in zip(s, t):

            # If c1 is already mapped, it must map to the same c2
            if c1 in mp1 and mp1[c1] != c2:
                return False

            # If c2 is already mapped, it must map back to the same c1
            if c2 in mp2 and mp2[c2] != c1:
                return False

            # Store both mappings
            mp1[c1] = c2
            mp2[c2] = c1

        # All mappings are valid
        return True
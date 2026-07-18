class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_mp = {}                             # HashMap for S
        t_mp = {}                             # HashMap for t
                        
        for ch in s:                          # Count frequency of characters in s
            s_mp[ch] = s_mp.get(ch, 0) + 1
        for ch in t:                          # Count frequency of characters in t
            t_mp[ch] = t_mp.get(ch, 0) + 1
        
        return s_mp == t_mp                  # Compare both dictionaries
       
        # first_str = Counter(s)             # Count Frequency using Counter()
        # second_str = Counter(t)            # Other Techinquie 
        # return first_str == second_str 
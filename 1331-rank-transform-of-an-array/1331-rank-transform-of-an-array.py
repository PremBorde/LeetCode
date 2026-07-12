class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Sort and Dublicate Remove
        sorted_element = sorted(set(arr))
        # Make Dictornary to store Rank 
        rank = {}
        for i , num in enumerate(sorted_element): # Store Index and Element - Iterate num in set
            rank[num] = i+1                       # rank[num] = Start from 1 index
        ans = []
        for num in arr:
            ans.append(rank[num])
        return ans
        



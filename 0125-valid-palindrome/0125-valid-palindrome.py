class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = []
        for x in s:     
            if x.isalnum():          # Check Actual Alphabets 
                t.append(x)          # Add only Alphabets 
       
        left = 0
        right = len(t)-1
        while left < right : 
            if t[left].lower() != t[right].lower():    # Check Alphabets converting in lowerCase
                return False                           # If any chacter doesnt match FALSE
            left +=1
            right -=1
        return True 


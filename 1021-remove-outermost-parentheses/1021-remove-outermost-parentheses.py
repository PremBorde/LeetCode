class Solution:
    def removeOuterParentheses(self, s: str) -> str:
 
        result = ""     # Empty String 
        count = 0       # Counter to check 

        for ch in s:
            if ch == '(':               # IF left (  
                count +=1               # Increase Count
                if count > 1:           # IF Count = 2
                    result += ch        # Append into result String  "("
            else:
                if ch == ")":           # If Right ) 
                    count -= 1          # Decrease Count 
                    if count > 0:       # IF Count 1 
                        result +=ch     # Append into result String  ")"
        return result                   # Final "(())"
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0          # First index
        right = n - 1     # Last index
        max_area = 0      # Maximum Area

        while left < right : 

            width = right - left                  # Widht Between left and Right Height
            h = min(height[left], height[right])  # Smaller Height 
            area = width * h                      # Current Maximum_Area 
            max_area = max(max_area, area)        # Updated Maximum_Area

            if height[left] < height[right]:      # Move to Smaller height  
                left +=1                          # Cause Choti height se pani overFlow nhi krega
            else:
                right -=1
        return max_area

class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0                    # Left pointer (Start se)
        right = len(height) - 1     # Right pointer (End se)
        leftMax = 0                 # Ab tak ka sabse bada left wall
        rightMax = 0                # Ab tak ka sabse bada right wall
        water = 0                   # Final Answer

        while left < right:                 
                                                 # Jo side choti hogi usi ko process karenge
            if height[left] < height[right]:     # Kyuki water level wahi decide kar sakte hai
                           
                if height[left] >= leftMax:      # Agar current wall leftMax se badi hai
                    leftMax = height[left]       # To new leftMax ban jayegi
                else:
                    water += leftMax - height[left]      # Warna yaha water store hoga
                                                          # Water = LeftMax - Current Height     
                left += 1                               # Left pointer aage badhao
            else:
                if height[right] >= rightMax:           # Same logic right side ke liye
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]   # Water = RightMax - Current Height
                right -= 1                              # Right pointer piche lao
                
        return water
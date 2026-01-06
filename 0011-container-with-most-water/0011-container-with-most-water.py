class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol=0
        l=0
        r=len(height) - 1
        
        while l < r:
            width=r - l
            current_area=width * min(height[l], height[r])
            
            max_vol=max(max_vol, current_area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_vol
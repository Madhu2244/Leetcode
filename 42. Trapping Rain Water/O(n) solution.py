class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        left, right = 0, len(height) - 1
        maxLeft,maxRight = height[left], height[right]
        
        while (left < right):
            if maxLeft < maxRight:
                left += 1 
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    volume += maxLeft - height[left]
            else:
                right -= 1
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    volume += maxRight - height[right]
        return volume
            

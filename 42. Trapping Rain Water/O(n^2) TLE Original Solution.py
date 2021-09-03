class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        for i in range (1, len(height)-1):
            left = i - 1
            right = i + 1
            maxLeft = 0
            maxRight = 0
            leftTested = False
            rightTested = False
            while not leftTested or not rightTested:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                if left == 0:
                    leftTested = True
                else:
                    left -= 1
                if height[right] > maxRight:
                    maxRight = height[right]
                if right == len(height) - 1:
                    rightTested = True
                else:
                    right += 1
            minimum = min(maxLeft,maxRight)
            if minimum > height[i]:
                volume += minimum - height[i]
        return volume
    

class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        maxLeft = [0]
        for i in range (1, len(height)):
            maxLeft.append(max(height[0:i]))
        maxRight = [0]
        for i in range (len(height)-2,-1,-1):
            maxRight.insert(0,max(height[i+1:]))
        minValue = []
        for i in range (0, len(maxLeft)):
            minValue.append(min(maxLeft[i],maxRight[i]))
            # if height[i] < min(maxLeft[i],maxRight[i]):
            #     minValue.append(min(maxLeft[i],maxRight[i] - height[i]))
        # print(minValue)
        for i,n in enumerate(minValue):
            if height[i] <= n:
                volume += n - height[i]
        return volume

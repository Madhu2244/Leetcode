import math
class Solution:
    def solve(self, nums):
        left, right = 0, len(nums) - 1
        minimum = math.inf
        while (left <= right):
            mid = left + (right - left) // 2
            if nums[mid] > mid:
                right = mid - 1
            elif nums[mid] < mid:
                left = mid + 1
            else:
                minimum = mid
                right = mid - 1
        if minimum == math.inf:
            return -1
        return minimum

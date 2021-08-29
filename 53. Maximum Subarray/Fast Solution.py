import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
            maximum = nums[0]
            current_sum = 0
            for n in nums:
                current_sum += n
                maximum = max(maximum,current_sum)
                if current_sum < 0:
                    current_sum = 0
            return maximum

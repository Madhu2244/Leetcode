import math
class Solution:
    def jump(self, nums: List[int]) -> int: 
        @cache
        def recurse(cur_index):
            if cur_index >= len(nums) - 1:
                return 0
            if nums[cur_index] == 0:
                return math.inf
            return min(recurse(cur_index+i) for i in range (1, nums[cur_index]+1)) + 1
        return recurse(0)

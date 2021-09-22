class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1
        if i == 0:
            return True
        while True:
            j = i - 1
            while j >= 0:
                if j + nums[j] >= i:
                    i = j
                    break
                j -= 1
            if j == 0:
                return True
            if j == -1:
                return False

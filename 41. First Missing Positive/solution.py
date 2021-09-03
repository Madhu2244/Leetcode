class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = [0 for i in range(len(nums) + 1)]

        for n in nums:
            if n <= 0 or n > len(nums):
                continue
            seen[n] = 1

        for i,n in enumerate(seen[1:]):
            if n == 0:
                return i + 1

        return len(nums)+1

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        for i,n in enumerate(nums):
            if n < 0 or n >= len(nums):
                nums[i] = 0
        #print(nums)
        for i,n in enumerate(nums):
            if n > 0:
                original_value = n % len(nums)
                nums[original_value] += len(nums)
        #print(nums)
        for i in range(1,len(nums)):
            if nums[i] < len(nums):
                return i
        return len(nums)
                    
        # for i,n in enumerate(nums):
        #     if n == 0:
        #         return i + 1

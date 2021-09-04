class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def recurse(used_nums, used_indexes):
            if len (used_nums) == len(nums):
                if used_nums not in result:
                    result.append(used_nums)
            for i,n in enumerate(nums):
                if i in used_indexes:
                    continue
                recurse(used_nums+[n],used_indexes+[i])
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            used_nums = [nums[i]]
            used_indexes = [i]
            recurse(used_nums,used_indexes)

        return result

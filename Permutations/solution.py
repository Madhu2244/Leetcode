class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def recurse(used_nums):
            if len(used_nums) == len(nums):
                result.append(used_nums)
                return
            for n in nums:
                if n in used_nums:
                    continue
                copy_used_nums = used_nums.copy()
                copy_used_nums.append(n)
                recurse(copy_used_nums)
        for n in nums:
            used_nums = [n]
            recurse(used_nums)
        return result

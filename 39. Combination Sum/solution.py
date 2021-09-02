class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def recurse(total: int,result_array: List[int]):
            if total == target:
                result.append(result_array)
                return
            for nums in candidates:
                if total + nums > target:
                    break
                if nums < result_array[-1]:
                    continue
                recurse(total+nums,result_array+[nums])
        for num in candidates:
            recurse(num,[num])
        return result

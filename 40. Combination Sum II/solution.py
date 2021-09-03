class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def recurse(total: int, used_numbers: List[int], current_index: int):
            if total == target:
                result.append(used_numbers)
                return
            current_index += 1
            localmin = current_index
            while current_index < len(candidates):
                if current_index > localmin and candidates[current_index] == candidates[current_index-1]:
                    current_index += 1
                    continue
                else:
                    cur_num = candidates[current_index]
                    if total + cur_num > target:
                        return
                    recurse(total+cur_num,used_numbers+[cur_num],current_index)
                    current_index += 1
        for current_index,nums in enumerate(candidates):
            if current_index > 0 and nums == candidates[current_index - 1]:
                    continue
            recurse(nums,[nums],current_index)
        return result

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        result_dict = []
        def recurse(total: int,result_array: List[int], dictionary_values: dict):
            if total == target:
                if dictionary_values in result_dict:
                    return
                result.append(result_array)
                result_dict.append(dictionary_values)
                return
            for nums in candidates:
                if total + nums > target:
                    continue
                copy = dictionary_values.copy()
                copy[nums] += 1
                recurse(total+nums,result_array+[nums],copy)
            
        for num in candidates:
            dictionary_values = collections.defaultdict(int)
            dictionary_values[num] +=1
            recurse(num,[num],dictionary_values)
        return result

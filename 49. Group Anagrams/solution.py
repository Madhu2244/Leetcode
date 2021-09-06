class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in range(len(strs)):
            a = ''.join(sorted(strs[i]))
            if a in result:
                result[a].append(strs[i])
            else:
                result[a] = [strs[i]]
        output = []
        for arr in result:
            output.append(result[arr])
        return output
                    

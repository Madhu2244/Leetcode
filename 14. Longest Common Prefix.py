class Solution(object):
    def longestCommonPrefix(self, strs):
        minlen = sys.maxint
        i = 0
        while (i < len(strs)):
            if len(strs[i]) < minlen:
                minlen = len(strs[i])
            i = i + 1
        print(minlen)
        i = 0
        x = 0
        result = ''
        
        while i < minlen:
            x = 0
            str = ''
            for words in strs:
                if x == 0:
                    str = words[0:i+1]
                elif words[0:i+1] != str:
                    return result
                x = x + 1
            result = str
            print(result)
            i = i + 1
        return result
        """
        :type strs: List[str]
        :rtype: str
        """
        

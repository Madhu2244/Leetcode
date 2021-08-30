class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        arr = list(map(int,list(digits)))
        d = {
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z']
        }
        result = []
        def backtrack(self, i: int, curStr: str):
            if len(curStr) == len(digits):
                result.append(curStr)
                return
            else:
                for k in d[int(digits[i])]:
                    backtrack(self,i+1,curStr + k)
        backtrack(self,0,'')
        return result
        
            

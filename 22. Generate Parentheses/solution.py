class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def recurse(cur_str: string, open_brackets: int, closed_brackets: int):
            if len(cur_str) == n * 2:
                result.append(cur_str)
                return
            if open_brackets < n:
                recurse(cur_str+'(', open_brackets + 1, closed_brackets)
            if closed_brackets + 1 <= open_brackets:
                recurse(cur_str+')', open_brackets, closed_brackets + 1)
        recurse('(',1,0)
        return result

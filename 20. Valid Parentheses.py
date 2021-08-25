"""
stack

if its ( { [, add to stack
if its ) } ], pop stack, check if its matching with the opposite type of parenthesis, if its not return false, else continue
return true
"""

class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                checker = stack.pop()
                if checker == '(':
                    if char == ')':
                        continue
                    else:
                        return False
                if checker == '{':
                    if char == '}':
                        continue
                    else:
                        return False
                if checker == '[':
                    if char == ']':
                        continue
                    else:
                        return False
        if len(stack) == 0:
            return True
        return False
        """
        
        :type s: str
        :rtype: bool
        """
        

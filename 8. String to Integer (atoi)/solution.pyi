import math
class Solution:
    def myAtoi(self, s: str) -> int:
        #1. remove whitespace
        s = s.strip() 
        #2. check if length is 0
        if len(s) == 0:
            return 0
        #2. check if positive or negative
        positive = False if s[0] == '-' else True
        #3. building the number
        num = ''
        for i,n in enumerate(s):
            if i == 0 and (n == '-' or n == '+'):
                continue
            if n.isnumeric():
                num += n
            else:
                break
        #4 converting to an int
        if len(num) == 0:
            num = int(0)
        num = int(num)
        #5 checking if its 32 bit range
        exponent_number = 2147483648
        if not positive:
            if (num >= exponent_number):
                return -exponent_number
            else:
                return -num
        if (num > exponent_number-1):
            return exponent_number-1
        return num
        

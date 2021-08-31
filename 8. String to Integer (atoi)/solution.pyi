import math
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        print(s)
        if len(s) == 0:
            return 0
        positive = False if s[0] == '-' else True
        if len(s) >= 2:
            bothSigns = True if (s[0] == '-' or s[0] == '+') and (s[1] == '-' or s[1] == '+') else False
            if bothSigns:
                return 0
        print(positive)
        num = ''
        for i,n in enumerate(s):
            if i == 0 and (n == '-' or n == '+'):
                continue
            if n.isnumeric():
                num += n
            else:
                break
        print(num)
        if len(num) == 0:
            num = int(0)
        num = int(num)
        print(num)
        if not positive:
            if (num >= math.pow(2,31)):
                return int(math.pow(-2,31))
            else:
                return -int(num)
        if (num > math.pow(2,31)-1):
            return int(math.pow(2,31) - 1)
        return int(num)
        

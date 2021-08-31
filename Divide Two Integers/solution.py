import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        result = 0
        negative = False
        negative = True if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else False
        dividend = abs(dividend)
        divisor = abs(divisor)
        leftover = dividend
        while True:
            temp = divisor
            n = 0
            while temp <= leftover:
                temp = temp << 1
                n += 1
            if n > 0:
                n -= 1
                result += math.pow(2,n) 
            if n == 0:
                if negative:
                    return int(-result)
                return int(result)
            temp = temp >> 1
            leftover = leftover - temp

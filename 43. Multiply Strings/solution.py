import math
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        output = 0
        for k in range (len(num2)):
            for j in range (len(num1)):
                adder = (10 ** (j+k)) * int(num1[len(num1)-1-j]) * int(num2[len(num2)-1-k])
                output += adder
        return str(int(output))

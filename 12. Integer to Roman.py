class Solution(object):
    def intToRoman(self, num):
        numToRoman = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        result = ''
        while num != 0:
            for key in sorted(numToRoman.keys(), reverse=True):
                if num - key >= 0:
                    num = num - key
                    result = result + numToRoman[key]
                    break
        return result
        

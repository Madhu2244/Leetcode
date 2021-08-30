class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 0
        for i in range(len(digits)):
            digits[i] = digits[i] + 1
            if digits[i] % 10 == 0:
                digits[i] = 0
                if i == len(digits) - 1:
                    digits.append(1)
            else:
                break
        digits.reverse()
        return digits

"""
[1,2,3]

starting at the last index and going towards the front
at the very last index, just add one to it and mod the result by 10. 
calculate the reaminder using int division.
if remainder = 0, return
else
	nums[i] = (nums[i] + 1) % 10
	remainder 

"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = (digits[len(digits)-1] + 1) // 10
        digits[len(digits)-1] = (digits[len(digits)-1] + 1) % 10
        if remainder == 0:
            return digits
        #print(digits, remainder)
        for i in range (len(digits)-2,-1,-1):
            if remainder == 0:
                return digits
            remainder = (digits[i] + 1) // 10
            digits[i] = (digits[i] + 1) % 10
        if remainder == 0:
            return digits
        return [1] + digits

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

"""
initial O(n) thoughts:

0 0 1 1 1 2 2 3 3 4
if (len(nums) == 0):
	return 0
int k = 0
increment k for each element removed
O(n) complexity
int prev element = nums[0]
x = 0
shiftcounter = 0
while (x+shiftcounter) < len(nums):
	if x == 0:
		x++
		continue
	elif nums[x+shiftcounter] == prev element:
		k++
		shiftcounter++
		nums[x] = nums[x+1] (if nums[x+1] != prev element), otherwise continue 
		x++
	else:
		prev element = nums[x+shiftcounter]
return nums

0 0 1 1 1 2 2 3 3 4
prev element = 0
x = 0

0 < 10 check
x == 0 check
x - 1
contininue

1 < 10 check
nums[1] == prev element (0) check
k = 1
nums[1] = nums[2]
x = 2

2 < 10 check
nums[2] == prev element (0) false
so prev element = 1

3 < 10 check
nums[3] == prev element (1) true
k = 2
nums[3] = nums[4]


initial O(n) thoughts is getting too complicated, i might just go for a O(2n) run here so that everything is alot easier to read and understand
if len(nums) == 0:
	return 0
prevnum = nums[0]
deletenums = [false]
for (int i = 1; i < len(nums); i++) 
	if nums[i] == prevnum
		deletenums.append(true)
		nums[i] = None
	else:
		deletenums.append(false)
		prevnums = nums[i]
for (int i = 0; i < len(nums) i++)
	if nums[i] == None:
		nums[i:] = nums[i+1:]
"""

class Solution(object):
    def removeDuplicates(self, nums):
        #check if len is 0
        if len(nums) == 0:
            return 0
        #using i to loop through array
        i = 1
        prevnum = nums[0]
        while i < len(nums):
            if nums[i] == prevnum:
                nums[i:] = nums[i+1:]
                i = i -1
            else:
                prevnum = nums[i]
            i = i + 1
        print(nums)
        return len(nums)
        
        

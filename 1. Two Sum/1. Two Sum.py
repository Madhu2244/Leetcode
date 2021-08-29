class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        #initial pass to get values into dictionary
        for i,n in enumerate(nums):
            if n in d:
                d[n][0] += 1
                d[n][1].append(i)
            else:
                d[n] = [1,[i]]
        #print(d)
        
        
        #second pass to go through each element and check if the opposite is in the dictionary to add up to target
        for i,n in enumerate(nums):
            leftover = target - n
            #check if leftover value is in dictionary
            if leftover in d:
                #check if leftover value is the same as current index
                if leftover == n:
                    if d[leftover][0] > 1:
                        result = [i,d[leftover][1][1]]
                        break
                else:
                    result = [i,d[leftover][1][0]]
                    break
                          
        return result
"""
 ab

initially set both a pointer and b pointer to home
if: increasing b pointer increases the sum, go ahead
else: if: increasing b pointer makes the sum go below 0:
        if a pointer == b pointer
            increase both a pointer and b pointer
        else
            increase just a pointer
      else: increase b pointer
"""

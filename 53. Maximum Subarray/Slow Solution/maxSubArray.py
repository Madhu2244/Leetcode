import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
            maximum = nums[0]
            leftpointer = 0
            rightpointer = 0
            current_sum = nums[0]
            while True:
                if rightpointer < len(nums) -1:
                    if sum(nums[leftpointer:rightpointer+2]) > current_sum:
                        rightpointer += 1
                    elif sum(nums[leftpointer+1:rightpointer+1]) > current_sum and leftpointer != rightpointer:
                        leftpointer+=1
                    elif sum(nums[leftpointer:rightpointer+2]) <= 0:
                        if leftpointer == rightpointer:
                            leftpointer +=1
                            rightpointer +=1
                        else:
                            leftpointer +=1
                    else:
                        rightpointer +=1
                else:
                    if leftpointer >= len(nums) - 1:
                        break
                    else:
                        leftpointer +=1
                current_sum = sum(nums[leftpointer:rightpointer+1])
                maximum = max(current_sum,maximum)
            return maximum
                
                

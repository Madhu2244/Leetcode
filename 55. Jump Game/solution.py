class Solution:
    def canJump(self, nums: List[int]) -> bool:
        solution = [False] * len(nums)
        solution[0] = True
        i = 0
        while i < len(nums):
            if solution[len(nums)-1]:
                return True
            if solution[i] and i != len(nums)-1:
                for j in range(nums[i]+1):
                    if i + j >=len(nums):
                        break
                    solution[i+j] = True
                #print(solution)
                i += 1
            else:
                i += 1
                continue
        #print(solution)
        return solution[len(nums)-1]

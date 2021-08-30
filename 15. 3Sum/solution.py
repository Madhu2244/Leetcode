class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i,n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                target = 0 - n
                arr = nums[0:i]+nums[i+1:]
                left = i
                right = len(arr)-1
                while left < right:
                    if arr[left] + arr[right] > target:
                        right -= 1
                    elif arr[left] + arr[right] < target:
                        left += 1
                    else:
                        result.append([n,arr[left],arr[right]])
                        left += 1
                        while left <= len(arr)-1 and arr[left] == arr[left - 1]:
                            left += 1
        return result

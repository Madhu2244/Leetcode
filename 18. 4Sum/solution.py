class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = []
        for i in range (len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            arr = nums[i+1:]
            for j in range (len(arr)-2):
                if j > 0 and arr[j] == arr[j-1]:
                    continue
                print(nums[i],arr[j])
                left = j + 1
                right = len(arr)-1
                while left < right:
                    if arr[left] + arr[right] + nums[i] + arr[j] == target:
                        result.append([arr[left], arr[right], nums[i], arr[j]])
                        left += 1
                        while (left < len(arr) -1 and arr[left] == arr[left-1]):
                            left += 1
                    elif arr[left] + arr[right] + nums[i] + arr[j] > target:
                        right -= 1
                    else:
                        left +=1
        return result

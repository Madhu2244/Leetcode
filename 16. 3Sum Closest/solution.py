class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minimum = nums[0] + nums[1] + nums[2]
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            arr = nums[0:i] + nums[i+1:]
            print(arr)
            left = i
            right = len(arr) - 1
            while left < right:
                cur_sum= arr[left]+arr[right]+n
                if abs(cur_sum - target) < abs(minimum - target):
                    minimum = cur_sum
                if cur_sum > target:
                    right -= 1
                elif cur_sum < target:
                    left += 1
                else:
                    return target
        return minimum                

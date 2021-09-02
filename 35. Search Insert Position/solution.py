class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while (l <= r):
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        if nums[0] >= target:
            return 0
        if nums[-1] <= target:
            return len(nums)
        
        l,r = 0, len(nums)
        while (l <= r):
            mid = l + (r - l) // 2
            print(l,r,mid,nums[mid])
            if mid > 0:
                if mid < len(nums):
                    if nums[mid] > target and nums[mid-1] < target:
                        return mid 
                if nums[mid] > target and nums[mid-1] < target:
                    return mid - 1
            if mid < len(nums):
                if nums[mid] < target and nums[mid+1] > target:
                    return mid + 1
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            

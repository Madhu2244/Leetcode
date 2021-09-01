class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]: #this left portion is full sorted
                if target >= nums[left] and target <= nums[mid]: #target in left portion
                    right = mid - 1
                else: #target in right portion
                    left = mid + 1
            else: #right portion is full sorted
                if target >= nums[mid] and target <= nums[right]: #target in right portion
                    left = mid + 1
                else: #target in left portion
                    right = mid - 1
        return -1

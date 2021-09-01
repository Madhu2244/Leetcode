class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        #binary search to find the first element
        index_of_first_element = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                #if statement to check if nums[mid] == nums[mid-1]
                if mid > left and nums[mid] == nums[mid-1]:
                    right = mid - 1
                else:
                    index_of_first_element = mid
                    break
            elif nums[mid] > target: # currently on a spot to the right of target
                right = mid - 1
            else: # currently on a spot to the left of target
                left = mid + 1
        print(index_of_first_element)
        if index_of_first_element == -1:
            return [-1,-1]
        left = index_of_first_element + 1
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                #if statement to check if nums[mid] == nums[mid-1]
                if mid < right and nums[mid] == nums[mid+1]:
                    left = mid + 1
                else:
                    return [index_of_first_element,mid]
            elif nums[mid] > target: # currently on a spot to the right of target
                right = mid - 1
            else: # currently on a spot to the left of target
                left = mid + 1
        return [index_of_first_element,index_of_first_element]
        #return [-1,-1]

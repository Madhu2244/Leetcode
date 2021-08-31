class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i,n in reversed(list(enumerate(nums))):
            if n == val:
                nums.pop(i)
        return len(nums)

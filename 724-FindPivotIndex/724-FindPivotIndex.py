# Last updated: 7/15/2025, 4:46:52 PM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
     
        return -1





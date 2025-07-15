# Last updated: 7/15/2025, 4:47:03 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set(nums)
        if len(set1) == len(nums):
            return False
        else:
            return True

        
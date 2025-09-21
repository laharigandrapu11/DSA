# Last updated: 9/21/2025, 6:11:42 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        snums = set(nums)
        if len(snums) == len(nums):
            return False
        else:
            return True
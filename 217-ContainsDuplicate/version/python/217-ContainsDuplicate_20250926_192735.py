# Last updated: 9/26/2025, 7:27:35 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        snums = set(nums)
        if len(snums) == len(nums):
            return False
        else:
            return True
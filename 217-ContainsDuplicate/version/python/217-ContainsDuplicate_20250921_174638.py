# Last updated: 9/21/2025, 5:46:38 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
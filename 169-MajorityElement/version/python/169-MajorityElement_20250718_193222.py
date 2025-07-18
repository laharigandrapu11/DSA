# Last updated: 7/18/2025, 7:32:22 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        val = int(len(nums) / 2)
        return nums[val]

        
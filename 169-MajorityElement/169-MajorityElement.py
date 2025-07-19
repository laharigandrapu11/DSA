# Last updated: 7/19/2025, 3:19:06 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        val = int(len(nums) / 2)
        return nums[val]

        
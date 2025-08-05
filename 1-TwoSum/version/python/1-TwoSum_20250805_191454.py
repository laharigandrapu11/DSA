# Last updated: 8/5/2025, 7:14:54 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in h:
                h[nums[i]] = i
            else:
                return sorted([i,h[diff]])

        

        
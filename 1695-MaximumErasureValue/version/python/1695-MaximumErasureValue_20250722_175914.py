# Last updated: 7/22/2025, 5:59:14 PM
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # sortedNums = sorted(nums, reverse=True)
        # if sortedNums == nums:
        #     return -1
        maxSum = -1
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if i < j  and nums[i] < nums[j]:
                    curr = abs(nums[i] - nums[j])
                    maxSum = max(curr, maxSum)
        return maxSum

                 
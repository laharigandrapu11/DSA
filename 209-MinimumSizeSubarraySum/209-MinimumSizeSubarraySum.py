# Last updated: 7/15/2025, 4:47:05 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        totalSum = 0
        length = len(nums)+1
        L= 0
        for R in range(len(nums)):
            totalSum += nums[R]
            while totalSum>= target:
                length = min(length, R-L+1 )
                totalSum -= nums[L]
                L += 1
        if length == len(nums)+1:
            return 0
        else:
            return length
        
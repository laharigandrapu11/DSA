# Last updated: 7/15/2025, 4:47:01 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sums = sum(nums)
        n = len(nums)
        sumofn = n*(n+1)/2
        return int(sumofn-sums)
        
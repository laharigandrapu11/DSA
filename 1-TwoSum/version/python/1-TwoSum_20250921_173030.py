# Last updated: 9/21/2025, 5:30:30 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum1 = (n * (n+1))/2
        return int(sum1 - sum(nums))
        
# Last updated: 10/11/2025, 6:39:43 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms = nums[0]
        
        cu = 0
        for n in nums:
            cu = max(0, cu)
            cu += n
            ms = max(ms, cu)
        return ms
        
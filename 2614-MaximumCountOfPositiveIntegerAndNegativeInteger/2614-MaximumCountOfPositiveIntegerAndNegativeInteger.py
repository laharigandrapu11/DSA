# Last updated: 7/27/2025, 4:54:21 PM
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        nos, pos = 0,0
        for n in nums:
            if n<0:
                nos += 1
            elif n>0:
                pos += 1
            else:
                continue
        return max(nos, pos)
# Last updated: 10/2/2025, 7:11:51 PM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = {}
        for n in nums:
            if n in h:
                return n
            else:
                h[n] = 1
         
        
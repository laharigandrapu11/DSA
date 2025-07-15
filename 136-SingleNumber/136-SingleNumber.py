# Last updated: 7/15/2025, 4:47:09 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result
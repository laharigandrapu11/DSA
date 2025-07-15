# Last updated: 7/15/2025, 4:46:42 PM
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(i+2, len(nums)):
                    if i<j<k and nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        count+= 1
        return count

        
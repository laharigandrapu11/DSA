# Last updated: 7/15/2025, 4:46:36 PM
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target and i<j:
                    count+=1
        return count
        
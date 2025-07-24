# Last updated: 7/24/2025, 2:52:05 PM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                arr.append((nums[i]-1)*(nums[j]-1))
        return max(arr)
        
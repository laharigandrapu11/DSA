# Last updated: 7/15/2025, 5:48:25 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i in range(len(nums)):
                if(nums[i] == target):
                    return i
        else:
            nums.append(target)
            nums = sorted(nums)
            return nums.index(target)

            
        
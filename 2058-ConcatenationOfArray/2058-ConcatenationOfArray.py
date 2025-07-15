# Last updated: 7/15/2025, 4:46:43 PM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans+ans
        
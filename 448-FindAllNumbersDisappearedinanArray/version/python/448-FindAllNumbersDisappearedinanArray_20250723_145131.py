# Last updated: 7/23/2025, 2:51:31 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        present = set(nums)             
        return [i for i in range(1, len(nums)+1) if i not in present]

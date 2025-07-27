# Last updated: 7/27/2025, 4:54:39 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        present = set(nums)             
        return [i for i in range(1, len(nums)+1) if i not in present]

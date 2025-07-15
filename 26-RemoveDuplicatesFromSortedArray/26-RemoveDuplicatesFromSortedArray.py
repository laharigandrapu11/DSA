# Last updated: 7/15/2025, 5:48:27 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        nums[:len(unique)]= unique
        return len(unique)
        
        
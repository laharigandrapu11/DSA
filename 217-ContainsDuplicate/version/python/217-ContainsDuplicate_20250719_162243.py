# Last updated: 7/19/2025, 4:22:43 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nh = {}
        for n in nums:
            if n in nh:
                return True
            else:
                nh[n] = 1
        return False
        
        

        
# Last updated: 7/15/2025, 4:47:04 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        window = set()
        for j in range(len(nums)):
            if j-i>k:
                window.remove(nums[i])
                i += 1
                
            if nums[j] in window:
                print(nums[j])
                return True
         
            

            window.add(nums[j])
            
        return False
        
            
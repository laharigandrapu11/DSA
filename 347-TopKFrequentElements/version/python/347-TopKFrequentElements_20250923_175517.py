# Last updated: 9/23/2025, 5:55:17 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hl = {}
        for n in nums:
            if n in hl:
                hl[n] += 1
            else:
                hl[n] = 1
        keys_by_value = sorted(hl, key=hl.get,reverse=True)  
         
        return keys_by_value[:k]    
        
        
        
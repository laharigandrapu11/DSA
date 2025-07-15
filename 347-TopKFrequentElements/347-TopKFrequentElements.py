# Last updated: 7/15/2025, 4:46:58 PM
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
        
        
        
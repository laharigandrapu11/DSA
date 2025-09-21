# Last updated: 9/21/2025, 5:48:54 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap ={}
        for n in nums:
            if n in hashMap:
                return True
            else:
                hashMap[n] = 1
        return False
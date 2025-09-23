# Last updated: 9/22/2025, 8:14:29 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(s) == sorted(t) else False
        
# Last updated: 10/23/2025, 7:44:00 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
        
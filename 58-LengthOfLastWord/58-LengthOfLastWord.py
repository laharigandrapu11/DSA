# Last updated: 7/15/2025, 4:47:14 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        word = s.split()
        return len(word[-1])

        
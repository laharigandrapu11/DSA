# Last updated: 7/19/2025, 3:18:42 PM
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])
        
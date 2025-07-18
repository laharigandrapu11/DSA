# Last updated: 7/18/2025, 7:56:56 PM
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])
        
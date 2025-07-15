# Last updated: 7/15/2025, 4:46:44 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        comb = ""
        max_len = max(len(word1), len(word2))
        for i in range(max_len):
            if i < len(word1):
                comb += word1[i]
            if i < len(word2):
                comb += word2[i]
        return comb

        
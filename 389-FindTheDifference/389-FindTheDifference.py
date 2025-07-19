# Last updated: 7/19/2025, 3:18:56 PM
class Solution:
    def findTheDifference(self, s: str, t: str) -> None:
        h = {}
        for s in s:
            if s in h:
                h[s] += 1
            else:
                h[s] = 1
        for s in t:
            if s in h:
                h[s] += 1
            else:
                h[s] = 1
        for ch in h:
            if h[ch] % 2 == 1:
                return ch


# Last updated: 7/22/2025, 6:38:25 PM
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxIndex = 1
        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i] < colors[j]:
                    curr = abs(i - j)
                    maxIndex = max(curr, maxIndex)
        return maxIndex


        
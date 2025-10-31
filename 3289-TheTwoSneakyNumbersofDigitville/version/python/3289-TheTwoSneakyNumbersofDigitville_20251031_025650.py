# Last updated: 10/31/2025, 2:56:50 AM
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a = []
        h = {}
        for n in nums:
            if n in h:
                h[n] += 1
            else:
                h[n] = 1
        for n in h:
            if h[n] == 2:
                a.append(n)
        return a
        
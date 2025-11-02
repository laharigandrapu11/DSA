# Last updated: 11/1/2025, 9:21:45 PM
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        result = 0
        while l<=r:
            mid = (l+r) // 2
            if isBadVersion(mid):
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result
            

        
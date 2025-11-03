# Last updated: 11/2/2025, 7:03:50 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        nums = sorted(piles)
        l = 1
        r = nums[-1]
        print("h", h)
        while l<= r:
            mid = (l+r) // 2
            hours = 0
            for n in piles:
                if n <= mid:
                    hours += 1
                else:
                    hours += (n + mid - 1) // mid 
            if hours <= h:
                r = mid - 1
            elif hours > h:
                l = mid + 1
            else:
                return mid
        return l    






        
# Last updated: 11/13/2025, 9:13:56 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r) // 2
            if nums[mid] != target:
                if nums[l] > target:
                    l = l+1
                elif nums[l] < target:
                    if nums[mid] < target:
                        l = l + 1
                    else:
                        r = mid - 1
                else:
                    return l
            else:
                return mid
        return -1
                
        
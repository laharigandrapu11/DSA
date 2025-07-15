# Last updated: 7/15/2025, 5:48:13 PM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = set()
        for nums in nums1:
            if nums in nums2:
                arr.add(nums)
        return list(arr)
        
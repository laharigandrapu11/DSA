# Last updated: 7/15/2025, 4:47:11 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j = 0,0 
        while i <len(nums1) and j<len(nums2):
            if (nums1[i] == 0):
                nums1[i] = nums2[j]
                i+=1
                j+=1
            else:
                i+=1
        nums1.sort()

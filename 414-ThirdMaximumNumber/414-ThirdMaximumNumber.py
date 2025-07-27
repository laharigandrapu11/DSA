# Last updated: 7/27/2025, 4:54:40 PM
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr =  list(sorted(set(nums)))
        print(arr)
        arr = arr[::-1]
        print(arr)
        if(len(arr)<3):
            return arr[0]
        else:
            return arr[2]
        
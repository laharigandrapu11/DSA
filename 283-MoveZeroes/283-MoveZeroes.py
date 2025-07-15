# Last updated: 7/15/2025, 4:47:00 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        newArray = [] 
        for i in range(len(nums)):
            if(nums[i]!=0):
                newArray.append(nums[i])
                
            else:
                count+=1
                
            
        nums[:] = newArray + [0] * count
        
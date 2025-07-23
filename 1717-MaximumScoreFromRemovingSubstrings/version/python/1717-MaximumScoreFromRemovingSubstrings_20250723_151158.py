# Last updated: 7/23/2025, 3:11:58 PM
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if (nums[i] == nums[i + 1]) :
                nums[i] *= 2
                nums[i + 1] = 0
        # [1,4,0,2,0,0]
        print(nums)   
            
        count = 0
        newArray = [] 
        for i in range(len(nums)):
            if(nums[i]!=0):
                newArray.append(nums[i])
                
            else:
                count+=1
        nums = newArray + [0] * count
        return nums
        
        


             
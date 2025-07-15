# Last updated: 7/15/2025, 5:48:26 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        for num in nums:
            if(num == val):
                continue
            temp.append(num)
        for i in range(len(temp)):
            nums[i] = temp[i]
        return len(temp)            
            
        
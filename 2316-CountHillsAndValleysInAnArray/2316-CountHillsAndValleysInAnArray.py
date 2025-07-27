# Last updated: 7/27/2025, 4:54:22 PM
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        newlist = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i]!= nums[i-1]:
                newlist.append(nums[i])
        print(newlist)
        hill = 0
        valley = 0

        for i in range(1,len(newlist)-1):
                if newlist[i-1]<newlist[i] and newlist[i+1]<newlist[i]:
                    hill += 1
                elif newlist[i-1]>newlist[i] and newlist[i+1]>newlist[i]:
                    valley += 1

      
        return hill+valley

        
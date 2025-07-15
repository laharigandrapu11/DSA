# Last updated: 7/15/2025, 4:46:59 PM
class NumArray:

    def __init__(self, nums: List[int]):
        total = 0
        self.prefixSum = []
        for n in nums:
            total += n
            self.prefixSum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        rightVal = self.prefixSum[right]
        if left>0:
            leftVal = self.prefixSum[left-1] 
        else:
            leftVal = 0
        return rightVal - leftVal

        


        
       



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
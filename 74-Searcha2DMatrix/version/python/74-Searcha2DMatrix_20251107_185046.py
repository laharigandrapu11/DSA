# Last updated: 11/7/2025, 6:50:46 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> None:
        
        rows , cols = len(matrix), len(matrix[0])
        l, r = 0, rows*cols -1
        while l <= r:
            mid = (l+r) //2
            row, col = mid // cols , mid % cols
            guess = matrix[row][col]
            if target == guess:
                return True
            elif guess<target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        
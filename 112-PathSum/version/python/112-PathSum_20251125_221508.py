# Last updated: 11/25/2025, 10:15:08 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

       
        def backtrack(root, val, targetSum):
            if not root:
                return False
            val += root.val
            if not root.left and not root.right:
                if targetSum == val:
                    return True
            if backtrack(root.left, val, targetSum):
                return True
            if backtrack(root.right, val, targetSum):
                return True        
            val -= root.val
            return False
        return backtrack(root, 0, targetSum)

            
        
# Last updated: 12/1/2025, 6:44:32 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
9
10       
11        def backtrack(root, val, targetSum):
12            if not root:
13                return False
14            val += root.val
15            if not root.left and not root.right:
16                if targetSum == val:
17                    return True
18            if backtrack(root.left, val, targetSum):
19                return True
20            if backtrack(root.right, val, targetSum):
21                return True        
22            val -= root.val
23            return False
24        return backtrack(root, 0, targetSum)
25
26            
27        
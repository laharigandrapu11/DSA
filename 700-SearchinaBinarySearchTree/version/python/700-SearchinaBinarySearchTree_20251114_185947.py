# Last updated: 11/14/2025, 6:59:47 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val > val:
                return self.searchBST(root.left,val)
            elif root.val < val:
                return self.searchBST( root.right,val)
            else:
                return root
        return None

        
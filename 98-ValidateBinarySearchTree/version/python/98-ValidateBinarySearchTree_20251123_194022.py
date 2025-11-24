# Last updated: 11/23/2025, 7:40:22 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            values.append(root.val)
            inorder(root.right)
        inorder(root)
        values2 = sorted(values)
        for i in range(len(values2)):
            for j in range(len(values2)):
                if values2[i] == values2[j] and i != j:
                    return False
        return values == sorted(values)
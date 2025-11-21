# Last updated: 11/21/2025, 6:17:03 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        value =[]
        finalVal = []
        
        if root:
            queue.append(root)
        
        while (len(queue) > 0):
            sublist = []
            for i in range(len(queue)):
                curr = queue.popleft()
                sublist.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            value.append(sublist)  
        print(value)
        for i in range(len(value)):
            if len(value[i])>=1:
                finalVal.append(value[i][-1])


        return finalVal
        
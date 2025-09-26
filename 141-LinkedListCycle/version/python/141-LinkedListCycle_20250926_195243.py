# Last updated: 9/26/2025, 7:52:43 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h = {}
        curr = head
        while curr:
            if curr in h:
                return True
            else:
                h[curr] = 1
                curr = curr.next
        return False
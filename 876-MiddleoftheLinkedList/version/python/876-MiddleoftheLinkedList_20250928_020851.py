# Last updated: 9/28/2025, 2:08:51 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        curr = head
        while curr:
            l.append(curr)
            curr = curr.next
        mid = len(l) // 2
        return l[mid]
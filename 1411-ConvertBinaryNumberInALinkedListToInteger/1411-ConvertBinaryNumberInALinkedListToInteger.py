# Last updated: 7/15/2025, 4:46:48 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        string = ""
        while head is not None:
            string+=str(head.val)
            head = head.next
        return int(string,2)
        
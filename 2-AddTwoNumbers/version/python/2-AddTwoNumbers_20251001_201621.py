# Last updated: 10/1/2025, 8:16:21 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lt1 = ""
        lt2 = ""
        while l1:
            lt1+=(str(l1.val))
            l1 = l1.next
        while l2:
            lt2+=(str(l2.val))
            l2 = l2.next
        sumList = (int(lt1[::-1])+int(lt2[::-1]))

        dummy = head = ListNode()
        if sumList == 0:
            return ListNode(0)
        while sumList > 0:
            r = sumList % 10   
            sumList //= 10 
            head.next = ListNode(r)
            head = head.next
        return dummy.next
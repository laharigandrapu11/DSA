# Last updated: 10/10/2025, 6:26:46 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast, slow2 = head, head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
                
        if fast == None or fast.next == None:
            return None
        
        while slow2!=slow:
            slow2 = slow2.next
            slow = slow.next
        return slow
                
                    
                

                
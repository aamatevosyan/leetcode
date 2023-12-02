# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        slow, fast = head, head.next
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            
            fast = fast.next
        
        slow.next = None

        return head
        
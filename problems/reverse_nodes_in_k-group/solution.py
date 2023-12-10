# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode], tail: Optional[ListNode]):
        curr, prev = head, None

        while curr and curr != tail:
            _next = curr.next

            curr.next = prev
            prev = curr
            curr = _next
        
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        a = b = head
        for _ in range(k):
            if not b:
                return head
            
            b = b.next
        
        reversed_b = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)

        return reversed_b
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        prev = dummy = ListNode(0, head)

        for _ in range(left - 1):
            prev = prev.next
        
        curr = prev.next

        left_prev, left_curr = prev, curr

        for _ in range(right - left + 1):
            _next = curr.next

            curr.next = prev
            prev = curr
            curr = _next

        left_prev.next = prev
        left_curr.next = curr

        return dummy.next
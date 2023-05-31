# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow.next

        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next

        slow.next = None
        
        one, two = head, prev
        while two:
            _next = one.next
            one.next = two
            one = two
            two = _next

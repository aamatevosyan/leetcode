# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        _len = 0
        curr = head

        while curr:
            _len += 1
            curr = curr.next
        
        curr, prev = head, None
        k, i = _len - n + 1, 1

        while curr and curr.next and i < k:
            prev = curr
            curr = curr.next
            i += 1

        if not prev:
            head = head.next
        else:
            prev.next = curr.next
        
        return head
        
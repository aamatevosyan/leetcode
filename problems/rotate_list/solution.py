# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        _len, end = 1, head

        while end.next:
            _len += 1
            end = end.next
        
        end.next = head
        
        k = k % _len
        prev, curr = end.next, head

        for i in range(_len - k):
            prev = curr
            curr = curr.next
        
        prev.next = None

        return curr


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        start = ListNode(next=head)
        curr, before, after = head, start, None

        while curr and curr.next:
            after = curr.next.next
            first, second = curr, curr.next

            second.next = first
            first.next = after
            before.next = second

            curr = after
            before = first
        
        return start.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_lt = curr_lt = ListNode()
        dummy_gte = curr_gte = ListNode()
        curr = head

        while curr:
            if curr.val < x:
                curr_lt.next = curr
                curr_lt = curr_lt.next
            else:
                curr_gte.next = curr
                curr_gte = curr_gte.next
            
            curr = curr.next
        
        curr_gte.next = None
        curr_lt.next = dummy_gte.next

        return dummy_lt.next
        
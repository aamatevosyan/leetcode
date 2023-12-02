# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findFromEnd(self, head: ListNode, k: int) -> ListNode:
        curr = head

        for _ in range(k):
            curr = curr.next
        
        end = head
        while curr:
            end = end.next
            curr = curr.next
        
        return end
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        x = self.findFromEnd(dummy, n + 1)
        x.next = x.next.next

        return dummy.next
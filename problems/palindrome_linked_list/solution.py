# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, before, after = head, None, None

        while curr:
            after = curr.next
            curr.next = before
            before = curr
            curr = after

        return before

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next
        
        curr = head
        slow = self.reverse(slow)

        while slow:
            if curr.val != slow.val:
                return False
            
            curr = curr.next
            slow = slow.next
        
        return True
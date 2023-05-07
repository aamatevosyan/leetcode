# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if not node:
            return None
        
        curr, before, after = node, None, None
        
        while curr:
            after = curr.next
            curr.next = before
            before = curr
            curr = after
            
        return before
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans, remainer = ListNode(), 0
        curr = ans
        
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        
        while l1 or l2 or remainer:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            
            raw_sum = first + second + remainer
            digit, remainer = raw_sum % 10, raw_sum // 10
            
            curr.next = ListNode(digit)
            curr = curr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return self.reverse(ans.next)
            
        
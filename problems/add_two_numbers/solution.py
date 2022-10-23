# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]):
        cur, prev = head, None

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1, r2 = l1, l2

        divider, current = 0, 0

        head = ListNode(0)
        result = head

        while r1 and r2:
            local_sum = r1.val + r2.val + divider

            reminder = local_sum % 10
            divider = local_sum // 10

            tmp = ListNode(reminder)
            head.next = tmp

            head = tmp

            r1 = r1.next
            r2 = r2.next

        while r1:
            local_sum = r1.val + divider

            reminder = local_sum % 10
            divider = local_sum // 10

            tmp = ListNode(reminder)
            head.next = tmp

            head = tmp
            r1 = r1.next

        while r2:
            local_sum = r2.val + divider

            reminder = local_sum % 10
            divider = local_sum // 10

            tmp = ListNode(reminder)
            head.next = tmp

            head = tmp
            r2 = r2.next
        
        if divider > 0:
            tmp = ListNode(divider)
            head.next = tmp

            head = tmp
        
        return result.next
        


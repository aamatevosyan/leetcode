# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        
        if list2 is None or (list1 and list1.val < list2.val):
            head = ListNode(list1.val)
            list1 = list1.next
        else:
            head = ListNode(list2.val)
            list2 = list2.next

        cur = head

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            
            cur = cur.next
        
        while list1:
            cur.next = ListNode(list1.val)
            list1 = list1.next
            cur = cur.next
        
        while list2:
            cur.next = ListNode(list2.val)
            list2 = list2.next
            cur = cur.next

        return head
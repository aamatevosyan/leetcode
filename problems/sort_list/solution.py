# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        curr, arr = head, []
        
        while curr:
            arr.append(curr)
            curr = curr.next
        
        arr.sort(key=lambda node: node.val)

        _head, prev = arr[0], arr[0]

        for i in range(1, len(arr)):
            prev.next = arr[i]
            prev = arr[i]
        
        prev.next = None

        return _head



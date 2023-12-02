from heapq import heapify

ListNode.__lt__= lambda self, other: self.val < other.val

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        q = [node for node in lists if node is not None]
        heapify(q)

        while q:
            node = heappop(q)
            
            curr.next = ListNode(node.val)
            curr = curr.next

            if node.next:
                heappush(q, node.next)

        return dummy.next
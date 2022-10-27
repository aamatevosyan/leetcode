from heapq import heappush, heappop

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for root in lists:
            if root:
                heappush(minHeap, Node(root))
        
        head, tail = None, None
        while minHeap:
            node = heappop(minHeap).node

            if not head:
                head = tail = node
            else:
                tail.next = node
                tail = tail.next
            
            if node.next:
                heappush(minHeap, Node(node.next))

        return head
        
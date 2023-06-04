from queue import PriorityQueue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node(ListNode):
    @classmethod
    def wrap(cls, node: 'ListNode'):
        return cls(val=node.val, next=node.next)

    def __lt__(self, other: 'Node'):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = head = ListNode()
        heap = PriorityQueue()

        for node in lists:
            if node:
                heap.put(Node.wrap(node))

        while not heap.empty():
            node = heap.get()
            curr.next = ListNode(node.val)
            curr = curr.next

            if node.next:
                heap.put(Node.wrap(node.next))

        return head.next

        